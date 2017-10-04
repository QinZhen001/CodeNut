#ifndef SANDBOX_H
#define SANDBOX_H

#include <seccomp.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/wait.h>
#include <sys/resource.h>
#include <sys/time.h>
#include <unistd.h>
#include <time.h>
#include <pthread.h>
#include <fcntl.h> 
#include "tools.h"

#define TIMETOP (60)
#define MEMTOP (128 * 1024 * 1024)
#define STACKTOP (32 * 1024 * 1024)

#define REPORTER puts

typedef struct LimitList {
	int time_limit;
	int memory_limit;
} LimitList;


typedef struct RunConfig {
    char** args;
	char* output;
	char* language;
	LimitList limit_list;
} RunConfig;


typedef struct RunResult {
	int time_used;
	int memory_used;
	int run_signal;
	int return_code;
} RunResult;

typedef struct KillerArgs {
    pid_t pid;
    int timeout;
} KillerArgs;

int load_c_cpp_syscall_list(const RunConfig *run_config) {
	int syscalls_whitelist[] = {SCMP_SYS(read),  SCMP_SYS(readlink),
				            SCMP_SYS(close), SCMP_SYS(mprotect),
				            SCMP_SYS(write), SCMP_SYS(arch_prctl),
				            SCMP_SYS(writev),SCMP_SYS(brk),
				            SCMP_SYS(access),SCMP_SYS(exit_group),
				            SCMP_SYS(mmap),  SCMP_SYS(fstat),
				            SCMP_SYS(munmap),SCMP_SYS(sysinfo),
							SCMP_SYS(uname), SCMP_SYS(lseek),
							SCMP_SYS(time), SCMP_SYS(set_thread_area)};
	int syscalls_whitelist_length = sizeof(syscalls_whitelist) / sizeof(int);

	scmp_filter_ctx ctx = NULL;
	// load seccomp rules
	ctx = seccomp_init(SCMP_ACT_KILL);
	
	if (! ctx) {
		REPORTER("Initialize system call failed");
		return -1;
	}
	
	for (int i = 0; i < syscalls_whitelist_length; i++) {
		if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, syscalls_whitelist[i], 0) != 0) {
			REPORTER("Add system call failed");
			return -1;
		}
	}

	// add extra rule for execve
	if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(execve), 1, 
		SCMP_A0(SCMP_CMP_EQ, (scmp_datum_t)run_config -> args[0])) != 0) {
		REPORTER("Add system call failed");
		return -1;
	}

	// do not allow open("w" and "rw")
	if (seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(open), 1,
		SCMP_CMP(1, SCMP_CMP_MASKED_EQ, O_WRONLY | O_RDWR, 0)) != 0) {
		REPORTER("Add system call failed");
		return -1;
	}
	
	if (seccomp_load(ctx) != 0) {
		REPORTER("Load system call failed");
		return -1;
	}

	seccomp_release(ctx);
	return 0;
}


int load_general_syscall_list(const RunConfig *run_config) {
	REPORTER(run_config -> language);
	// linux use 'strace' to print all program sys call
	int syscalls_blacklist[] = {SCMP_SYS(fork), SCMP_SYS(vfork)};

	int syscalls_blacklist_length = sizeof(syscalls_blacklist) / sizeof(int);

	scmp_filter_ctx ctx = NULL;
	// load seccomp rules
	ctx = seccomp_init(SCMP_ACT_ALLOW);
	
	if (! ctx) {
		REPORTER("Initialize system call failed");
		return -1;
	}

	for (int i = 0; i < syscalls_blacklist_length; i++) {
		if (seccomp_rule_add(ctx, SCMP_ACT_KILL, syscalls_blacklist[i], 0) != 0) {
			REPORTER("Add system call failed");
			return -1;
		}
	}
	// add extra rule for execve
    if (seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execve), 1,
    	SCMP_A0(SCMP_CMP_NE, (scmp_datum_t)run_config -> args[0])) != 0) {
		REPORTER("Add execve call failed");
		return -1;
    }
    // do not allow open("w" and "rw" )
    if (seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(open), 1,
    	SCMP_CMP(1, SCMP_CMP_MASKED_EQ, O_WRONLY, O_WRONLY)) != 0) {
		REPORTER("Add open call failed");
		return -1;
    }
    /* java error
    if (seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(open), 1,
    	SCMP_CMP(1, SCMP_CMP_MASKED_EQ, O_RDWR, O_RDWR)) != 0) {
		REPORTER("Add open call failed");
		return -1;
    }
    */
    // do not allow openat("w" and "rw")
    if (seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(openat), 1,
    	SCMP_CMP(2, SCMP_CMP_MASKED_EQ, O_WRONLY, O_WRONLY)) != 0) {
		REPORTER("Add openat call failed");
		return -1;
    }
    if (seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(openat), 1,
    	SCMP_CMP(2, SCMP_CMP_MASKED_EQ, O_RDWR, O_RDWR)) != 0) {
		REPORTER("Add openat call failed");
		return -1;
	}
		
	if (seccomp_load(ctx) != 0) {
		REPORTER("Load system call failed");
		return -1;
	}

	seccomp_release(ctx);
	return 0;
}

	
int load_limit(const RunConfig *run_config) {
	struct rlimit rtmp;
	
	rtmp.rlim_max = TIMETOP;
	rtmp.rlim_cur = (rlim_t)(run_config -> limit_list.time_limit * 1.3 / 1000) + 1 < rtmp.rlim_max ?
					(rlim_t)(run_config -> limit_list.time_limit * 1.3 / 1000) + 1 : rtmp.rlim_max;
	if (setrlimit(RLIMIT_CPU, &rtmp) != 0) {
		REPORTER("Load cpu time limit failed");
		return -1;
	}

	if (strcmp(run_config -> language, "Java") != 0
		&& strcmp(run_config -> language, "JavaScript") != 0) { // Java and JavaScript do not limit
		rtmp.rlim_max = MEMTOP;
		rtmp.rlim_cur = (rlim_t)2 * run_config -> limit_list.memory_limit * 1024 * 1024 < rtmp.rlim_max ?
						(rlim_t)2 * run_config -> limit_list.memory_limit * 1024 * 1024 : rtmp.rlim_max;
		if (setrlimit(RLIMIT_AS, &rtmp) != 0) {
			REPORTER("Load memory limit failed");
			return -1;
		}
	}

	rtmp.rlim_max = STACKTOP;
	rtmp.rlim_cur = (rlim_t)2 * run_config -> limit_list.memory_limit * 1024 * 1024 < rtmp.rlim_max ?
					(rlim_t)2 * run_config -> limit_list.memory_limit * 1024 * 1024 : rtmp.rlim_max;
	if (setrlimit(RLIMIT_STACK, &rtmp) != 0) {
		REPORTER("Load stack size limit failed");
		return -1;
	}

	return 0;
}


void child_process(const RunConfig *run_config){
  	if (freopen(run_config -> output, "a", stdout) == NULL) {
		REPORTER("Freopen out failed");
		exit(1);
	}
	
	if (freopen(run_config -> output, "a", stderr) == NULL) {
		REPORTER("Freopen err failed");
		exit(1);
	}

	if (load_limit(run_config) != 0) exit(1);
	if (strcmp(run_config -> language, "C") == 0
		|| strcmp(run_config -> language, "C++") == 0) {
		if (load_c_cpp_syscall_list(run_config) != 0) exit(1);
	}
	else {
		if (load_general_syscall_list(run_config) != 0) exit(1);
	}

	REPORTER("prepare execute subroutine");
	if (execve(run_config -> args[0], run_config -> args, NULL) == -1) {
		REPORTER("Execve failed");
		exit(1);
	}

	exit(0);
}

void *timeout_killer(void *KillerArgs) {
    // this is a new thread, kill the process if timeout
    pid_t pid = ((struct KillerArgs *)KillerArgs)->pid;
    int timeout = ((struct KillerArgs *)KillerArgs)->timeout;
    // On success, pthread_detach() returns 0; on error, it returns an error number.
    if (pthread_detach(pthread_self()) != 0) {
        kill(pid, SIGKILL);
        return NULL;
    }
    // usleep can't be used, for time args must < 1000ms
    // this may sleep longer that expected, but we will have a check at the end
    if (sleep((unsigned int)((timeout + 1000) / 1000)) != 0) {
        kill(pid, SIGKILL);
        return NULL;
    }
    if (kill(pid, SIGKILL) != 0) {
        return NULL;
    }
    return NULL;
}

int runner(const RunConfig *run_config, RunResult *run_result) {
	// record current time
    struct timeval start, end;
	gettimeofday(&start, NULL);

	pid_t child_pid = fork();
	
	if (child_pid < 0) {
		REPORTER("Main fork failed");
		return -1;
	}
	else if (child_pid == 0) {
    	child_process(run_config);
	}
	else {
		// create new thread to monitor process running time
		pthread_t monitor_tid = 0;

		struct KillerArgs killer_args;
		killer_args.pid = child_pid;
		killer_args.timeout = run_config -> limit_list.time_limit * 1.3;
		if (pthread_create(&monitor_tid, NULL, timeout_killer, (void *) (&killer_args)) != 0) {
            kill(child_pid, SIGKILL);
			REPORTER("Pthread failed");
        }

        int status;
        struct rusage resource_usage;

		// wait for child process to terminate
        // on success, returns the process ID of the child whose state has changed;
        // On error, -1 is returned.
        if (wait4(child_pid, &status, WSTOPPED, &resource_usage) == -1) {
			REPORTER("Wait child failed");
			return -1;
		}

		// get end time
        gettimeofday(&end, NULL);

		if (pthread_cancel(monitor_tid) != 0) {
			REPORTER("Wait monitor failed");
			return -1;
		}
		
		if (WIFSIGNALED(status) != 0) run_result -> run_signal = WTERMSIG(status);
		run_result -> return_code = WEXITSTATUS(status);
		run_result -> time_used = (int) (end.tv_sec * 1000
										+ end.tv_usec / 1000
										- start.tv_sec * 1000
										- start.tv_usec / 1000);
		run_result -> memory_used = (int)(resource_usage.ru_maxrss);
	}
	return 0;
}

#endif

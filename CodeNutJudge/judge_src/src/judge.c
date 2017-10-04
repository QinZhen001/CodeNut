#include <string.h>
#include <sys/stat.h>
#include "sandbox.h"

typedef struct Result {
	char* status;
	int time_used;
	int memory_used;
} Result;


typedef struct Config {
	char** args;
	char* output;
	char* language;
	int time_limit;
	int memory_limit;
} Config;


void delete_all(Result *result, Config *config) {
	if (result -> status != NULL) free(result -> status);
    //The caller is not responsible for deallocating the buffer
}


Result run(Config *config) {
	char* status = (char*)malloc(sizeof(char) * 32);
	strcpy(status, "System Error");

	Result result = {status, 0, 0};

	RunResult run_result = {0, 0, 0, 0};

	RunConfig run_config = {config -> args, config -> output, config -> language,
	                    	{config -> time_limit, config -> memory_limit}};

	if (runner(&run_config, &run_result) != 0) {
		REPORTER("Run program failed");
		return result;
	}

	result.time_used = run_result.time_used;
	result.memory_used = run_result.memory_used;

	if (run_result.run_signal == 0) {
		if (run_result.return_code == 0) {
			strcpy(status, "Run Successfully");
		} else {
			strcpy(status, "Runtime Error");
		}
		if (run_result.time_used > config -> time_limit) {
			strcpy(status, "Time Limit Exceed");
		} else if (run_result.memory_used > config -> memory_limit) {
			strcpy(status, "Memory Limit Exceed");
		}
	} else if (run_result.run_signal == 31) {
		strcpy(status, "Dangerous System Call");
	} else if (run_result.run_signal == 9) {
		if (run_result.time_used > config -> time_limit) {
			strcpy(status, "Time Limit Exceed");
		} else {
			strcpy(status, "Runtime Error");
		}
	} else if (run_result.run_signal == 11) {
		if (run_result.memory_used > config -> memory_limit) {
			strcpy(status, "Memory Limit Exceed");
		} else {
			strcpy(status, "Runtime Error");
		}
	} else {
		if (run_result.time_used > config -> time_limit) {
			strcpy(status, "Time Limit Exceed");
		} else if (run_result.memory_used > config -> memory_limit) {
			strcpy(status, "Memory Limit Exceed");
		} else {
			strcpy(status, "Runtime Error");
		}
	}
	result.status = status;

	return result;
}


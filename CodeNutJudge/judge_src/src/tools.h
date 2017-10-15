#ifndef TOOLS_H
#define TOOLS_H
/*
REPORTER: write message in xx.log
READFILE: file -> val
*/

#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <time.h>

void REPORTER(char *log_info) {
  FILE *stream;
  stream = fopen("../log/CodeNutJudge.log", "a+");

  time_t now_time;
  time(&now_time);

  char output_time[32];
  // format time
  // %F: YYYY-MM-DD, %R: HH:MM, %S: second
  strftime(output_time, sizeof(output_time), "%F %R:%S", localtime(&now_time));
  // write format time into file stream
  fprintf(stream, "[%s] : %s. ErrorCode : %d\n", output_time, log_info, errno);
  fclose(stream);
}

#endif

#include <cstdio>
#include <iostream>
#include <unistd.h>

int main(int argc, char *argv[]) {
  fork();
  int a = atoi(argv[1]);
  int b = atoi(argv[2]);
  printf("%d %d %d\n", a, b, a + b);
  return 0;
}

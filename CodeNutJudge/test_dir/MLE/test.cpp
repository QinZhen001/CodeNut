#include <cstdio>
#include <iostream>

int c[30000000];

int main(int argc, char *argv[]) {
  for (int i = 1; i < 30000000; i++)
    c[i] = i;
  int a = atoi(argv[1]);
  int b = atoi(argv[2]);
  printf("%d %d %d\n", a, b, a + b);
  return 0;
}

#include <cstdio>
#include <iostream>

int a[1000];

int main(int argc, char *argv[]) {
  for (int i = 1; i <= 100000; i++)
    a[i] = i;
  int a = atoi(argv[1]);
  int b = atoi(argv[2]);
  printf("%d %d %d\n", a, b, a + b);
  return 0;
}

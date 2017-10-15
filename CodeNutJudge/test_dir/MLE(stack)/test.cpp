#include <cstdio>
#include <iostream>

int res;

int dfs(int de) {
  int i = de;
  if (de < 1000000000000) {
    res = dfs(de + 1);
  } else {
    return 0;
  }
  return i;
}

int main(int argc, char *argv[]) {
  dfs(0);
  int a = atoi(argv[1]);
  int b = atoi(argv[2]);
  printf("%d %d %d\n", a, b, a + b);
  return 0;
}

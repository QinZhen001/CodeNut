#include <cstdio>
#include <iostream>

int main(int argc, char* argv[]) {
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    printf("%d %d %d %d\n", a, a, b, a + b);
    return 0;
}

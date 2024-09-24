#include <cmath>
#include <iostream>
#include "watchtime.h"

#ifdef level
    #define OPTIMIZE __attribute__((optimize(level)))
#else
    #define OPTIMIZE
#endif

const int reps = 100000000; // number of times a test is repeated (for a single measurement)

void test1(int N) {
    int i = 0;
    while (i < N) {
        i++;
    }
}

void stats(unsigned time) {
    testtime = ((float)time / (float)reps);
    testtime *= 1000000; // ms to ns
    printf(",%.2f", testtime);
}

int main(int argc, char **argv) {
    int i, j;
    unsigned times[nms], aux;
    Watchtime time;

    int N;
    if (argc == 2) {
        N = atoi(argv[1]);
    } else {
        N = 50;
    }

    printf("\"Loop condition vs. Break sentence\"");
    printf(",\"%s\"", argv[0]);
    printf(",\"%d\"", N);
    printf(",%s", level);

    time.startTime();
    for (j = 0; j < reps; j++) {
        test1(N);
    }
    aux = time.getTime();

    stats(aux);
    printf("\n");
}

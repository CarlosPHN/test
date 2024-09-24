#include <cmath>
#include <iostream>
#include "watchtime.h"

#ifdef level
#define OPTIMIZE __attribute__((optimize(level)))
#else
#define OPTIMIZE
#endif

const int nms = 10; // number of measurements
const int reps = 100000000; // number of times a test is repeated (for a single measurement)

void test1(int N) {
    int i = 0;
    while (i < N) {
        i++;
    }
}

void test2(int N) {
    int i = 0;
    while (true) {
        i++;
        if (i >= N) break;
    }
}

void stats(unsigned times[]) {
    unsigned totaltime, meantime, sumsq, sd;
    float testtime;
    totaltime = meantime = sumsq = 0;
    for (int i = 0; i < nms; i++) {
        printf(",%lu", times[i]);
        totaltime += times[i];
    }
    meantime = totaltime / nms;
    for (int i = 0; i < nms; i++) {
        sumsq += (times[i] - meantime) * (times[i] - meantime);
    }
    sd = sqrt(sumsq / (nms - 1));
    testtime = ((float)meantime / (float)reps);
    testtime *= 1000000; // ms to ns
    printf(",%lu", meantime);
    printf(",%lu", sd);
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

    for (i = 0; i < nms; i++) {
        time.startTime();
        for (j = 0; j < reps; j++) {
            test1(N);
        }
        aux = time.getTime();
        times[i] = aux;
    }
    stats(times);

    for (i = 0; i < nms; i++) {
        time.startTime();
        for (j = 0; j < reps; j++) {
            test2(N);
        }
        aux = time.getTime();
        times[i] = aux;
    }
    stats(times);
    printf("\n");
}

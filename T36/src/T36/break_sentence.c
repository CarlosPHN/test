#include <cmath>
#include <iostream>
#include "watchtime.h"

const int reps = 100000000; // number of times a test is repeated (for a single measurement)

void test(int N) {
    int i = 0;
    while (true) {
        i++;
        if (i >= N) break;
    }
}

void stats(unsigned time) {
    float testtime;
    testtime = ((float)time / (float)reps);
    testtime *= 1000000; // ms to ns
    printf(",%.2f", testtime);
}

int main(int argc, char **argv) {
    int i, j;
    unsigned aux;
    Watchtime time;

    int N;
    if (argc == 2) {
        N = atoi(argv[1]);
    } else {
        N = 50;
    }

    printf(",\"%s\"", argv[0]);
    printf(",\"%d\"", N);

    time.startTime();
    for (j = 0; j < reps; j++) {
        test(N);
    }
    aux = time.getTime();

    stats(aux);
    printf("\n");
}

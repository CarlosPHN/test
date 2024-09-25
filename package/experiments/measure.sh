#!/bin/bash

EXPERIMENT="e1"
EXECUTABLE="break_sentence"

RAPLCOMMNAND="./$EXPERIMENT/exec/$EXECUTABLE"

modprobe msr
RAPL/main "$RAPLCOMMNAND" measurement "$EXPERIMENT/$EXECUTABLE"
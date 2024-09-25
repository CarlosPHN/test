#!/bin/bash

EXPERIMENT="e1"
EXECUTABLE="break_sentence"

RAPLCOMMNAND="/package/$EXPERIMENT/exec/$EXECUTABLE"

modprobe msr
/package/RAPL/main "$RAPLCOMMNAND" measurement "$EXPERIMENT/$EXECUTABLE"
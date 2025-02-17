#!/bin/bash
set -e 
set -o pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"
source $DIR/common.sh

setup "$1"


WORKLOAD_NAME="llm"


###############
# LLM Benchmark
###############

echo "Running llm benchmark"

clear_stats_entries "${WORKLOAD_NAME}_$1"

add_miralis_stat_entry "${WORKLOAD_NAME}_$1"

RemoteExec $ADDRESS "./llama.cpp/build/bin/llama-bench -m model.gguf" > "results/${WORKLOAD_NAME}_$1.txt"

add_miralis_stat_entry "${WORKLOAD_NAME}_$1"

echo "Done with llm benchmark"

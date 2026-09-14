#!/bin/bash
set -e
source /opt/conda/etc/profile.d/conda.sh
conda activate cellprofiler
export JAVA_HOME=/opt/conda/envs/cellprofiler
export "PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True" && cellprofiler
read -rsp $"Press enter to continue..."
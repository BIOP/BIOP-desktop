#!/bin/bash
source activate cellprofiler
export "PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True" && cellprofiler
read -rsp $"Press enter to continue..."
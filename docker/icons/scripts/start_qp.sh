#!/usr/bin/env bash
export LD_LIBRARY_PATH=/opt/conda/envs/djl/lib:/opt/conda/envs/djl/lib/python3.12/site-packages/torch/lib:$LD_LIBRARY_PATH
export PYTORCH_LIBRARY_PATH=/opt/conda/envs/djl/lib/python3.12/site-packages/torch/lib
export PYTORCH_VERSION=2.7.1
export PYTORCH_FLAVOR=cu126
exec /opt/QuPath/bin/QuPath -q -Djna.library.path=/opt/conda/envs/djl/lib
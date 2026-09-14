#!/bin/bash
set -e
source /opt/conda/etc/profile.d/conda.sh
conda activate devbio
naparia
read -rsp $"Press enter to continue..."
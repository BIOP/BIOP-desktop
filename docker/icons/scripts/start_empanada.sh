#!/bin/bash
set -e
source /opt/conda/etc/profile.d/conda.sh
conda activate empanada
napari
echo
read -rsp "Press enter to close..."
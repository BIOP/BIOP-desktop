#!/bin/bash
set -e
source /opt/conda/etc/profile.d/conda.sh
conda activate napari
napari
echo
read -rsp "Press enter to close..."
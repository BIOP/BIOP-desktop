#!/bin/bash
set -e
source /opt/conda/etc/profile.d/conda.sh
conda activate brainrender
napari
read -rsp $"Press enter to continue..."
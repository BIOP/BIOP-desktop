#!/bin/bash
set -e
source /opt/conda/etc/profile.d/conda.sh
conda activate samapi
python -m uvicorn samapi.main:app --workers 2
read -rsp $"Press enter to continue..."
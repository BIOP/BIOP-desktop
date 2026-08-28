#!/bin/bash
set -e
source /opt/conda/etc/profile.d/conda.sh
conda activate abba_python
python /opt/abba/abba_run.py
echo
read -rsp "Press enter to close..."
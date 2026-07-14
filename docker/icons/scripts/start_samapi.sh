#!/bin/bash
source activate samapi
python -m uvicorn samapi.main:app --workers 2
read -rsp $"Press enter to continue..."
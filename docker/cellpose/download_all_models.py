
from cellpose import models

MODEL_LIST = [ 'cpsam' ]

for m in MODEL_LIST:
    print(m)
    models.CellposeModel(model_type=m)
    print("=====")

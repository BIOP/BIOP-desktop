
from cellpose import models
import wget
import os

OUTPUT_DIRECTORY ="/home/biop/.cellpose/models/"
#os.mkdir(OUTPUT_DIRECTORY)

MODEL_LIST = [ 'cyto3' , 'tissuenet_cp3' ,'livecell_cp3','yeast_PhC_cp3','yeast_BF_cp3','bact_phase_cp3','bact_fluor_cp3','deepbacs_cp3','cyto2_cp3',
                'cyto2' , 'cyto', 'nuclei' ]

WGET_LIST = [ "size_cyto3.npy" , "size_cyto2torch_0.npy", "size_cytotorch_0.npy" , "size_nucleitorch_0.npy" ,
             'denoise_cyto3', 'deblur_cyto3', 'upsample_cyto3', 'oneclick_cyto3', 
             'denoise_cyto2', 'deblur_cyto2', 'upsample_cyto2', 'oneclick_cyto2', 
             'denoise_nuclei', 'deblur_nuclei', 'upsample_nuclei', 'oneclick_nuclei']

#WGET_LIST = ["cytotorch_0", "cyto2torch_0", "size_cytotorch_0.npy","size_cytotorch_0", "size_cyto2torch_0.npy","size_cyto2torch_0.npy", "size_cyto3.npy","size_cyto3",
#               "cyto_0", "nuclei_0", "size_cyto_0.npy", "size_nuclei_0.npy" ,"CP", "CPx", "TN1", "TN2", "TN3", "LC1", "LC2", "LC3", "LC4", "style_choice.npy"]

for m in MODEL_LIST:
    print(m)
    models.CellposeModel(model_type=m)
    print("=====")
    
for w in WGET_LIST:
    url = "https://www.cellpose.org/models/"+w
    print(url)
    wget.download(url, out=OUTPUT_DIRECTORY)
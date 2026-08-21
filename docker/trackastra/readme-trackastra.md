

# Latest Version

## build

```
docker build -f trackastra/Dockerfile-trackastra  -t biop-trackastra:v0.5.5 . --no-cache
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-trackastra:v0.5.5
```

## after testing pass, tag 
```
docker tag  biop-trackastra:v0.5.5  biop/biop-trackastra:v0.5.5 
```

## push on dockerhub
```
docker push biop/biop-trackastra:v0.5.5
```

# TESTs


## test GPU is available
from terminal :

```
conda activate trackastra
python
import torch
torch.cuda.is_available()
```

## test napari plugin is available
from terminal :

```
conda activate trackastra
napari 
```

From the GUI : 
- Plugins "Trackastra tracking"
- `File > Open Sample> trackastra > bacteria`
- Click Track


## test CLI

```
conda activate trackastra && cd /home/biop/.spotiflow/test_trackastra/ && trackastra track \
    --imgs Fluo-N2DL-HeLa/01 \
    --masks Fluo-N2DL-HeLa/01_ST/SEG \
    --model-pretrained general_2d \
    --output-ctc Fluo-N2DL-HeLa/01_RES \
    --device cuda
```
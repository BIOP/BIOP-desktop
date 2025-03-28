# Latest Version

## build
```
docker build -f cellpose/Dockerfile-cellpose  -t biop-cellpose:3.1.1.1 . --no-cache
```
## start to test (see below)
```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-cellpose:3.1.1.1
```

## after testing pass, tag 
```
docker tag  biop-cellpose:3.1.1.1 biop/biop-cellpose:3.1.1.1
```

## push on dockerhub
```
docker push biop/biop-cellpose:3.1.1.1
```

# Test(s)

## cellpose on blob
Upload `blobs.tif` to /home/biop/

Terminal :
```
source activate cellpose
python -Xutf8 -m cellpose --dir /home/biop/ --pretrained_model cyto3 --chan 0 --chan2 1 --diameter 30 --verbose --save_tif --no_npy --use_gpu 
```



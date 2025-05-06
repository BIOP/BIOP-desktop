# Latest Version

## build
```
docker build -f yolo/Dockerfile-yolo  -t biop-yolo:8.3.119 . --no-cache
```
## start to test (see below)
```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind   biop-yolo:8.3.119
```

## after testing pass, tag 
```
docker tag   biop-yolo:8.3.119 biop/biop-yolo:8.3.119
```

## push on dockerhub
```
docker push biop/biop-yolo:8.3.119
```

# Test(s)

## yolo on blob
Upload `blobs.jpg` to /home/biop/

```
source activate yolo
yolo task=detect mode=predict model=yolov8n.pt source=blobs.jpg
``` 


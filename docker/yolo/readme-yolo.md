# Latest Version

## build
```
docker build -f yolo/Dockerfile-yolo  -t biop-yolo:8.4.131 . --no-cache
```
## start to test (see below)
```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind   biop-yolo:8.4.131
```

## after testing pass, tag 
```
docker tag   biop-yolo:8.4.131 biop/biop-yolo:8.4.131
```

## push on dockerhub
```
docker push biop/biop-yolo:8.4.131
```

# Test(s)

## yolo on blob
Upload `blobs.jpg` to /home/biop/

```
conda activate yolo && yolo task=detect mode=predict model=yolov8n.pt source=blobs.jpg
``` 


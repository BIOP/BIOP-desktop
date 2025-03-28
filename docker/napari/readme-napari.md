# Latest Version

## build

```
docker build -f napari/Dockerfile-napari  -t biop-napari:0.5.6 .
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind biop-napari:0.5.6
```

## after testing pass, tag 
```
docker tag biop-napari:0.5.6 biop/biop-napari:0.5.6
```

## push on dockerhub
```
docker push biop/biop-napari:0.5.6
```

# Test(s)

- Start Napari using icon on the desktop
- Open a sample image


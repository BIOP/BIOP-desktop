

# Latest Version

## build

```
docker build -f spotiflow/Dockerfile-spotiflow  -t biop-spotiflow:v0.5.8 . --no-cache
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-spotiflow:v0.5.8 
```

## after testing pass, tag 
```
docker tag  biop-spotiflow:v0.5.8  biop/biop-spotiflow:v0.5.8 

docker tag  biop-spotiflow:v0.5.8 registry.rcp.epfl.ch/ptbiop/biop-spotiflow:v0.5.8

```

## push on dockerhub
```
docker push biop/biop-spotiflow:v0.5.8 



# data from OMERO 

https://omero.epfl.ch/webclient/?show=dataset-11228

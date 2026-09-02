# Latest Version

# biop-qupath:v0.7.0-only

## build

```
docker build -f QuPath/Dockerfile-qupath  -t biop-qupath:v0.7.0-only . --no-cache
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-qupath:v0.7.0-only
```

## after testing pass, tag 
```
docker tag  biop-qupath:v0.7.0-only biop/biop-qupath:v0.7.0-only
```

## test on cluster 


# biop-djl:0.36.0-cu126

## build

```
docker build -f QuPath/Dockerfile-djl --no-cache --pull   --build-arg CUDA_FLAVOR=cu126  --build-arg PYTORCH_VERSION=2.7.1 --build-arg CUDA_CUDART_LABEL=cuda-12.6.3 -t biop-djl:0.36.0-cu126  .
```

## start to test (see below)
```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-djl:0.36.0-cu126
```

## test on cluster 
```
docker tag  biop-djl:0.36.0-cu126 registry.rcp.epfl.ch/ptbiop/biop-djl:0.36.0-cu126
docker push registry.rcp.epfl.ch/ptbiop/biop-djl:0.36.0-cu126
```

## after testing pass, tag & push on dockerhub

```
docker tag  biop-djl:0.36.0-cu126 biop/biop-djl:0.36.0-cu126
```

```
docker push biop/biop-djl:036-cu126
```

# biop-qupath:v0.7.0-only

## build

```
docker build -f QuPath/Dockerfile-qupath-full  -t biop-qupath:v0.7.0-01-full . --no-cache
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-qupath:v0.7.0-01-full
```

## after testing pass, tag 

## test on cluster 
```
docker tag biop-qupath:v0.7.0-01-full registry.rcp.epfl.ch/ptbiop/biop-qupath:v0.7.0-01-full
docker push registry.rcp.epfl.ch/ptbiop/biop-qupath:v0.7.0-01-full
```

## push on dockerhub
```
docker tag  biop-qupath:v0.7.0-01-full biop/biop-qupath:v0.7.0-01-full
docker push biop/biop-qupath:v0.7.0-01-full
```

# Test(s)

## biop-qupath:v0.7.0-only

### QuPath - OMERO 

- Create a qupath project
- Open an OMERO server
- Import an image

## biop-djl:036-cu126

### InstanSeg

- Create a qupath project
- Open an OMERO server
- Import an image
- Make an annotation and run InstanSeg (GPU)  on it using GUI

## biop-qupath:v0.7.0-full

- Make an annotation and run : 
    - [x] cellpose, template script , with 'cyto3' and 'cpsam'
    - [x] stardist, template script , with '2D_versatile_fluo' 
    - [x] instanseg , GPU via GUI
    - [x] sam, using GUI
    - [x] spotiflow, template script

# Latest Version

## build

```
docker build -f QuPath/Dockerfile-qupath  -t biop-qupath:v0.6.0-only . --no-cache
```

```
docker build -f QuPath/Dockerfile-qupath-full  -t biop-qupath:v0.6.0-full . --no-cache
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-qupath:v0.6.0-only
```

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-qupath:v0.6.0-full
```


## after testing pass, tag 
```
docker tag  biop-qupath:v0.6.0-only biop/biop-qupath:v0.6.0-only
```

```
docker tag  biop-qupath:v0.6.0-full biop/biop-qupath:v0.6.0-full
```

## push on dockerhub
```
docker push biop/biop-qupath:v0.6.0-only
```

```
docker push biop/biop-qupath:v0.6.0-full
```

# Test(s)

biop-qupath:v0.6.0-only

## QuPath - OMERO 

- Create a qupath project
- Open an OMERO server
- Import an image

biop-qupath:v0.6.0-full

## cellpose

- Make an annotation and run : 
    - cellpose template script on it (commment the line as needed), with 'cyto3' and 'cpsam'
    - stardist
    - instanseg
    - sam

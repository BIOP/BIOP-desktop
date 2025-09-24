# Latest Version

## build

```
docker build -f QuPath/Dockerfile-qupath  -t biop-qupath:v0.6.0 . --no-cache
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-qupath:v0.6.0
```

## after testing pass, tag 
```
docker tag  biop-qupath:v0.6.0 biop/biop-qupath:v0.6.0
```

## push on dockerhub
```
docker push biop/biop-qupath:v0.6.0
```

# Test(s)

## QuPath - OMERO 

- Create a qupath project
- Open an OMERO server
- Import an image

## cellpose

- Make an annotation and run : 
    - cellpose template script on it (commment the line as needed), with 'cyto3' and 'cpsam'
    - stardist
    - instanseg

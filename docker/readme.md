
# To build

## Base image
```
docker build -f Dockerfile-base  -t biop-vnc-base:a.b.c . --no-cache
```
## BIOP-desktop image
```
docker build -f Dockerfile-ms  -t biop-desktop:a.b.c . --no-cache
```

## Block image
```
docker build -f blockName\Dockerfile-block  -t biop-block:a.b.c . --no-cache
```


# To run 

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind biop-desktop:a.b.c
```

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind biop-block:a.b.c
```



## build 
```
docker build -f abba/deepslice/Dockerfile-deepslice  -t biop-deepslice:1.1.5-01 . --no-cache
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-deepslice:1.1.5-01
```

## after testing pass, tag 
```
docker tag  biop-deepslice:1.1.5-01 biop/biop-deepslice:1.1.5-01
```

## push on dockerhub
```
docker push biop/biop-deepslice:1.1.5-01
```
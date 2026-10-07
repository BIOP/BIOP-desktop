# Latest Version

## build
```
docker build -f ilastik/Dockerfile-ilastik  -t biop-ilastik:1.4.2-gpu . --no-cache
```
## start to test (see below)
```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-ilastik:1.4.2-gpu
```

## after testing pass, tag 
```
docker tag  biop-ilastik:1.4.2-gpu biop/biop-ilastik:1.4.2-gpu
```

## push on dockerhub
```
docker push biop/biop-ilastik:1.4.2-gpu
```

# Test(s)
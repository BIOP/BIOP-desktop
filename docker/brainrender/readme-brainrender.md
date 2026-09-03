# Latest Version

## build
```
docker build -f brainrender/Dockerfile-brainrender  -t biop-brainrender:2.2.1 . --no-cache
```
## start to test (see below)
```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-brainrender:2.2.1
```

## after testing pass, tag 
```
docker tag  biop-brainrender:2.2.1 biop/biop-brainrender:2.2.1
```

## push on dockerhub
```
docker push biop/biop-brainrender:2.2.1
```

# Test(s)

## brainrender workflow
- Start brainrender (icon on desktop)
- Load atlas
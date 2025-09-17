# Latest Version

## build
```
docker build -f brainrender/Dockerfile-brainrender  -t biop-brainrender:0.1.3 . --no-cache
```
## start to test (see below)
```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-brainrender:0.1.3
```

## after testing pass, tag 
```
docker tag  biop-brainrender:0.1.3 biop/biop-brainrender:0.1.3
```

## push on dockerhub
```
docker push biop/biop-brainrender:0.1.3
```

# Test(s)

## brainrender workflow
- Start brainrender (icon on desktop)
- Load atlas
# Latest Version

## build
```
docker build -f cellprofiler/Dockerfile-cellprofiler  -t biop-cellprofiler:4.2.8-plugins . --no-cache
```
## start to test (see below)
```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-cellprofiler:4.2.8-plugins
```

## after testing pass, tag 
```
docker tag  biop-cellprofiler:4.2.8-plugins biop/biop-cellprofiler:4.2.8-plugins
```

## push on dockerhub
```
docker push biop/biop-cellprofiler:4.2.8-plugins
```

# Test(s)


# Latest Version

## build
```
docker build -f cellprofiler/Dockerfile-cellprofiler  -t biop-cellprofiler:4.2.8-01-plugins . --no-cache

docker build -f cellprofiler/Dockerfile-cellprofiler-test  -t biop-cellprofiler:4.2.8-01-plugins-ms . 
```
## start to test (see below)
```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-cellprofiler:4.2.8-01-plugins

docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-cellprofiler:4.2.8-01-plugins-ms
```

## after testing pass, tag 
```
docker tag  biop-cellprofiler:4.2.8-01-plugins  registry.rcp.epfl.ch/ptbiop/biop-cellprofiler:4.2.8-01-plugins
docker push registry.rcp.epfl.ch/ptbiop/biop-cellprofiler:4.2.8-01-plugins



docker tag  biop-cellprofiler:4.2.8-01-plugins biop/biop-cellprofiler:4.2.8-01-plugins
```

## push on dockerhub
```
docker push biop/biop-cellprofiler:4.2.8-01-plugins
```

# Test(s)


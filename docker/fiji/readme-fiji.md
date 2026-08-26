# Latest Version

## build

```
docker build -f fiji/Dockerfile-fiji  -t biop-fiji:20260826 . --no-cache

docker build -f fiji/Dockerfile-fiji-mini  -t biop-fiji-mini:20260826 .
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-fiji:20260826

```

## after testing pass, tag 
```
docker tag  biop-fiji:20260826  biop/biop-fiji:20260826
```

## push on dockerhub

```
docker push biop/biop-fiji:20260826
```

# Test(s)

## cellpose on blob

[x] use BIOP Fiji wrapper

## StarDist on blob

[x] use BIOP plugin
[x] works in 3D 
[x] works in in 2d

## Trackastra

Work in TrackMate after defining conda path in Fiji preferences


## Deconvolution GPU

to test one needs to push on RCP cluster (openCL not supported on WSL2 (yet) )

```
docker tag  biop-fiji:20260826  registry.rcp.epfl.ch/ptbiop/biop-fiji:20260826

docker push registry.rcp.epfl.ch/ptbiop/biop-fiji:20260826
```

## GPU deconvolution test on RCP cluster
- Create a RUNAI env
- Start a RUNAI workload
- Look for "clij deconv" in the search bar and RUN

## 3D script
- Open Fiji
- Open sample "T1 Head"
- Start plugins > 3D script > Interactive Animation


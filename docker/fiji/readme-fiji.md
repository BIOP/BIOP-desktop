# Latest Version

## build

```
docker build -f fiji/Dockerfile-fiji  -t biop-fiji:20261007 . --no-cache

docker build -f fiji/Dockerfile-fiji-mini  -t biop-fiji-mini:20260826 .
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  biop-fiji:20261007
```

## after testing pass, tag 
```
docker tag  biop-fiji:20261007  biop/biop-fiji:20261007
```

## push on dockerhub

```
docker push biop/biop-fiji:20261007
```

# Test(s)

## cellpose on blob

[x] use BIOP Fiji wrapper

## StarDist on blob

[x] use BIOP plugin
[x] works in 3D 
[x] works in in 2d

## Trackastra

Works in TrackMate after defining conda path in Fiji preferences

## openCL tools

### ON a Windows+WSL2 machine

To test one needs to push on RCP cluster (openCL not supported on WSL2 (yet) )

```
docker tag  biop-fiji:20260826  registry.rcp.epfl.ch/ptbiop/biop-fiji:20260826

docker push registry.rcp.epfl.ch/ptbiop/biop-fiji:20260826
```

next follow Linux machine section below

### Linux machine ( or cluster)

## GPU deconvolution 
- Open Fiji
- Look for "clij deconv" in the search bar and RUN

## 3D script
- Open Fiji
- Open sample "T1 Head"
- Start plugins > 3D script > Interactive Animation


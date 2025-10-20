# Latest Version

## build

```
docker build -f fiji/Dockerfile-fiji  -t biop-fiji:20251020 . --no-cache
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-fiji:20251020 
```

## after testing pass, tag 
```
docker tag  biop-fiji:20251020  biop/biop-fiji:20251020
```

## push on dockerhub

# TODO
```
docker push biop/biop-fiji:20251020
```

# Test(s)

## cellpose on blob

use Fiji wrapper

## StarDist on blob

use Fiji official plugin

## Deconvolution GPU

to test one needs to push on RCP cluster (openCL not supported on WSL2 (yet) )

```
docker tag  biop-fiji:20251020  registry.rcp.epfl.ch/ptbiop/biop-fiji:20251020 
```

```
docker push registry.rcp.epfl.ch/ptbiop/biop-fiji:20251020 
```

- Create a RUNAI env
- Start a RUNAI workload
- Look for "clij devon" in the search bar and RUN


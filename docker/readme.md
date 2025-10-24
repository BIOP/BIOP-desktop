
# To build

## Base image
```
docker build -f Dockerfile-base  -t biop-vnc-base:0.2.2 . --no-cache
```

## start to test (see below)
```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind biop/biop-vnc-base:0.2.2 
```

# Latest Version biop/biop-desktop:0.2.0

## build

```
docker build -f Dockerfile-ms  -t biop-desktop:0.2.4. 
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind biop-desktop:0.2.4
```

## To test on RCP cluster
```
docker tag biop-desktop:0.2.4  registry.rcp.epfl.ch/ptbiop/biop-desktop:0.2.4
```

```
docker push registry.rcp.epfl.ch/ptbiop/biop-desktop:0.2.4
```

## after testing pass, tag 
```
docker tag biop-desktop:0.2.4 biop/biop-desktop:0.2.4
```

## push on dockerhub
```
docker push biop/biop-desktop:0.2.4
```

# TEST 0.2.4
[x] omero-insight
[x] vscode
[x] jupyterlab
[x] Fiji , stardist on blobs 
[x] Fiji , cellpose on blobs
[x] Fiji , deconvolution (on Cluster, can't work on WSL)
[x] QP : create project with OMERO image
[x] QP : SAMapi
[x] QP : cellpose
[x] QP : cellpose-sam
[x] QP : StarDist
[x] QP : InstanSeg
[x] ABBA benchmarck
[x] devbio starts
[x] devbio process image (on Cluster, can't work on WSL)
[x] empanadas starts
[x] empanadas process image 
[x] brainrender starts 
[x] brainrender load mouse atlas
[x] cellprofiler starts
[x] cellprofiler process image with cellpose
[x] ilastik starts
[x] yolo prediction on blobs
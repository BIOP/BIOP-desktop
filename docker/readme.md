
# To build

# Latest Version biop/biop-desktop:1.0.0

## build

```
docker build -f Dockerfile-ms  -t biop-desktop:1.0.0 .
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind biop-desktop:1.0.0
```

## To test on RCP cluster
```
docker tag biop-desktop:0.2.4  registry.rcp.epfl.ch/ptbiop/biop-desktop:1.0.0
```

```
docker push registry.rcp.epfl.ch/ptbiop/biop-desktop:1.0.0
```

## after testing pass, tag 
```
docker tag biop-desktop:1.0.0 biop/biop-desktop:1.0.0
```

## push on dockerhub
```
docker push biop/biop-desktop:1.0.0
```

# TEST biop-desktop:1.0.0
[x] omero-insight
[x] vscode
[x] jupyterlab, seaborn
[x] Fiji , stardist (BIOP wrapper) on blobs 
[x] Fiji , cellpose on blobs
[x] Fiji , deconvolution (on Cluster, can't work on WSL)
[x] QP : create project with OMERO image
[x] QP : SAMapi
[x] QP : cellpose
[x] QP : cellpose-sam
[x] QP : StarDist
[x] QP : InstanSeg
[ ] ABBA benchmarck // not supported in 1.0.0, waiting for new release of ABBA
[x] devbio starts
[x] devbio process image (on Cluster, can't work on WSL)
[x] empanadas starts
[x] empanadas process image 
[ ] brainrender starts // not supported in 1.0.0, waiting for new release of ABBA
[ ] brainrender load mouse atlas// not supported in 1.0.0, waiting for new release of ABBA
[x] cellprofiler starts
[x] cellprofiler process image with cellpose, GPU
[x] ilastik starts
[x] yolo prediction on blobs
[x] devbio starts, binarize "balls" image
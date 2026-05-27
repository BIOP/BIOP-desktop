
# To build

## Base image
```
docker build -f base-tiger/Dockerfile-base-tigervnc  -t biop-vnc-base:0.3.0 . --no-cache

docker build -f base-tiger/Dockerfile-base-tigervnc-minimal  -t biop-vnc-base:0.3.0-minimal . --no-cache


```

# To run
```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind   biop-vnc-base:0.3.0

docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind   biop-vnc-base:0.3.0-minimal
```

docker tag biop-vnc-base:0.3.0 biop/biop-vnc-base:0.3.0 


docker tag biop-vnc-base:0.3.0-minimal biop/biop-vnc-base:0.3.0-minimal 


## To test on RCP cluster
```
docker tag biop-vnc-base:0.3.0-minimal registry.rcp.epfl.ch/ptbiop/biop-vnc-base:0.3.0-minimal

docker tag biop-vnc-base:0.3.0-minimal-conda registry.rcp.epfl.ch/ptbiop/biop-vnc-base:0.3.0-minimal
```

```

docker push registry.rcp.epfl.ch/ptbiop/biop-vnc-base:0.3.0-minimal

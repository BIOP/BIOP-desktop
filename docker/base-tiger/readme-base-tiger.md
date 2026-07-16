
# To build

## Base image
```
docker build -f base-tiger/Dockerfile-base-tigervnc  -t biop-vnc-base:0.3.0 . --no-cache

```

# To run
```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind   biop-vnc-base:0.3.0

```

docker tag biop-vnc-base:0.3.0 biop/biop-vnc-base:0.3.0 
docker push biop/biop-vnc-base:0.3.0

## To test on RCP cluster

```
docker tag biop-vnc-base:0.3.0 registry.rcp.epfl.ch/ptbiop/biop-vnc-base:0.3.0
docker push registry.rcp.epfl.ch/ptbiop/biop-vnc-base:0.3.0
```


## Tests

[x] start mozilla firefox and check if it works
[x] start jupyter notebook , create a seaborn notebook, import seaborn as sns 
[x] start OMERO.insight connect 
[x] start visual studio code and check if it works
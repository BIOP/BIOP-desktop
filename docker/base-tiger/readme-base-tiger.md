
# To build

## Base image
```
docker build -f base-tiger/Dockerfile-base-tiger  -t biop-vnc-base:0.3.0- . 

docker build -f base-tiger/Dockerfile-base-tiger  -t biop-vnc-base:0.3.0-evo . --no-cache
```

# To run
```

docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/local,type=bind  biop-vnc-base:0.3.0 # is working 

docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/local,type=bind  biop-vnc-base:0.3.0-evo
```


docker tag biop-vnc-base:0.3.0 biop/biop-vnc-base:0.3.0


## To test on RCP cluster
```
docker tag biop-vnc-base:0.3.0 registry.rcp.epfl.ch/ptbiop/biop-vnc-base:0.3.0-epflldap
```

```
docker push registry.rcp.epfl.ch/ptbiop/biop-vnc-base:0.3.0-epflldap
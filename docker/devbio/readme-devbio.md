# Latest Version

## build

```
docker build -f devbio/Dockerfile-devbio  -t biop-devbio:0.11.0 .
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind biop-devbio:0.11.0
```

## after testing pass, tag 
```
docker tag biop-devbio:0.11.0 biop/biop-devbio:0.11.0
```

## push on dockerhub
```
docker push biop/biop-devbio:0.11.0
```

# Test(s)

- Start devbio using icon on the desktop
- Open a sample image


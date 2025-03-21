docker build -f samapi/Dockerfile-samapi  -t biop-samapi:0.6.1 . 

docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-samapi:0.6.1


// data from OMERO 
test square and dots


# Latest Version

## build

```
docker build -f samapi/Dockerfile-samapi  -t biop-samapi:0.6.1-01 . --no-cache
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-samapi:0.6.1
```

## after testing pass, tag 
```
docker tag  biop-samapi:0.6.1 biop/biop-samapi:0.6.1
```

## push on dockerhub
```
docker push biop/biop-samapi:0.6.1
```

# Test(s)

- Start `SAMAPI`, `QuPath`,
- Create a qupath project
- Open an OMERO server
- Import an image
- When the `SAMAPI` terminal is ready, start `QuPath-SAM-extension`
- Click `Live`
- Select `Rectangle` annotation and draw around your `Object Of Interest` 
- Repeat last step a few times


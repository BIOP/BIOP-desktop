# Latest Version

## build
```
docker build -f abba/Dockerfile-abba  -t biop-abba:0.11.0 . --no-cache
```

## start to test (see below)
```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-abba:0.11.0
```

## after testing pass, tag 
```
docker tag  biop-abba:0.11.0 biop/biop-abba:0.11.0
```

## push on dockerhub
```
docker push biop/biop-abba:0.11.0
```

# Test(s)

## ABBA workflow
- Start ABBA (icon on desktop)
- Look for ABBA benchmark and Run it
- Open QuPath (icon on desktop)
- Open project from /tmp/zip...
- Open an image (hosted on TIM OMERO) use credentials read-tim / read-tim 
- Load annotations on image


## Brainrender
- use the icon on desktop to start brainrender


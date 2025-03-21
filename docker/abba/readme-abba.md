# Latest Version

## build
```
docker build -f abba/Dockerfile-abba  -t biop-abba:0.10.6 . --no-cache
```
## start to test (see below)
```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-abba:0.10.6
```

## after testing pass, tag 
```
docker tag  biop-abba:0.10.6 biop/biop-abba:0.10.6
```

## push on dockerhub
```
docker push biop/biop-abba:0.10.6
```

# Test(s)

## ABBA workflow
- Start ABBA (icon on desktop)
- Look for ABBA benchmark

## Brainrender
- Start a `terminal`
- `source activate brainrender`
- `>napari`
- Go to `Plugins` -> `Brainrender` (and wait for it to load )


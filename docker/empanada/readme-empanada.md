# Latest Version

## build

```
docker build -f empanada/Dockerfile-empanada  -t biop-empanada:1.2.4 . 
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-empanada:1.2.4
```

## after testing pass, tag 
```
docker tag  biop-empanada:1.2.4 biop/biop-empanada:1.2.4
```

## push on dockerhub
```
docker push biop/biop-empanada:1.2.4
```

# Test(s)

- Start empanada using icon on the desktop
- Open a sample image
- Test 2D and 3D prediction




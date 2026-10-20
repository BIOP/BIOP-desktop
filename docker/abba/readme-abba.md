# Latest Version

## build
```
docker build -f abba/Dockerfile-abba  -t biop-abba:0.25.0 . --no-cache
```

## start to test (see below)
```
docker run -it --rm -p 8888:8888 --gpus device=0  -v /home/guiet/dockerstorage:/home/biop/local   biop-abba:0.25.0
```

## after testing pass, tag 
```
docker tag  biop-abba:0.25.0 biop/biop-abba:0.25.0
```

## push on dockerhub
```
docker push biop/biop-abba:0.25.0
```

# Test(s)

## ABBA workflow
- Start ABBA (icon on desktop)
- Look for ABBA benchmark and Run it
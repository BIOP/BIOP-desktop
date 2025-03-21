# Latest Version

## build

```
docker build -f leonardo/Dockerfile-leonardo  -t biop-leonardo:0.1.1-01 . 
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-leonardo:0.1.1 
```

## after testing pass, tag 
```
docker tag  biop-leonardo:0.1.1 biop/biop-leonardo:0.1.1
```

## push on dockerhub
```
docker push biop/biop-leonardo:0.1.1
```

# Test(s)

- Start leonardo using icon on the desktop
- Open a sample image
- Run DeStripe (1 min per slice on 1 GPU, on Ti2080)




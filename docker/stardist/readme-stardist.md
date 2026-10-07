# Latest Version

## build

```
docker build -f stardist/Dockerfile-stardist  -t biop-stardist:0.9.2 . --no-cache
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-stardist:0.9.2
```

## after testing pass, tag 
```
docker tag  biop-stardist:0.9.2  biop/biop-stardist:0.9.2

docker tag  biop/biop-stardist:0.9.2 registry.rcp.epfl.ch/ptbiop/biop-stardist:0.9.2

docker push registry.rcp.epfl.ch/ptbiop/biop-stardist:0.9.2
```

## push on dockerhub

```
docker push biop/biop-stardist:0.9.2
```

# Test(s)

## StarDist 2D

upload blob.tif 

- mamba run -n stardist stardist-predict2d -i /home/biop/blobs.tif -m 2D_versatile_fluo -o /home/biop/

## StarDist 3D

mamba run -n stardist stardist-predict3d -i /home/biop/local/BIOP-desktop/stardist/crop_Crop_ds441-c1.tif -m /home/biop/local/BIOP-desktop/stardist/n1_stardist_96 -o /home/biop/local/BIOP-desktop/stardist/output/ --n_tiles 4 4 4

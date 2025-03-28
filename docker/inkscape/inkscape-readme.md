# Latest Version

## build

```
docker build -f inkscape/Dockerfile-inkscape  -t biop-inkscape:0.1.4 . --no-cache
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-inkscape:0.1.4
```

## after testing pass, tag 
```
docker tag  biop-inkscape:0.1.4 biop/biop-inkscape:0.1.4
```

## push on dockerhub
```
docker push biop/biop-inkscape:0.1.4
```

# Test(s)

## ImageJ Macro Panel 

- Download the svg available at https://wiki-biop.epfl.ch/en/ipa/inkscape-figure#example
- Download the images available on [zenodo](https://zenodo.org/records/4248921)
- Open the svg with inkscape
- Select the image panel
- Open the object properties tab
- Update the image path
- Click on the "set" button
- Open the ImageJ panel in``Extensions > Figure > ImageJ Macro Panel...`  


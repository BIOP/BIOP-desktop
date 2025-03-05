docker build -f napari/Dockerfile-napari  -t biop-napari:0.5.6 .

docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind biop-napari:0.5.6

docker tag biop-napari:0.5.6 biop/biop-napari:0.5.6

docker push biop/biop-napari:0.5.6
```
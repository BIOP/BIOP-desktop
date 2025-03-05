
https://github.com/FZJ-INM1-BDA/celldetection-napari

docker build -f celldetection\Dockerfile-celldetection -t biop-celldetection:0.0.1 . 

docker run -it --rm -p 8888:8888 --gpus device=0 --mount src=D:/Docker/local_drive,target=/home/biop/local,type=bind biop-celldetection:0.1.0 

docker tag biop-celldetection:0.1.0 biop/biop-celldetection:0.1.0 
docker push biop/biop-celldetection:0.1.0
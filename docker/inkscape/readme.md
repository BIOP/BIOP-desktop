# inkscape docker

docker build -f inkscape/Dockerfile-inkscape  -t biop-inkscape:0.1.0 . 

docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind biop-inkscape:0.1.0
docker build -f QuPath/Dockerfile-qupath  -t biop-qupath:v0.5.1-02 . 

docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind biop-qupath:v0.5.1-02
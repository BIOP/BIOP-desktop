docker build -f openpiv/Dockerfile-openpiv -t biop/biop-openpiv:0.25.3 .

docker run -it --rm -p 8888:8888 --gpus device=0 --mount src=D:/,target=/home/biop/local,type=bind biop/biop-openpiv:0.25.3

docker tag biop-openpiv:0.25.3 biop/biop-openpiv:0.25.3 

docker push biop/biop-openpiv:0.25.3 

# Latest Version

## build
```
docker build -f tf2onnx/Dockerfile-tf2onnx  -t biop-tf2onnx:1.9.2 . --no-cache

```
## start to test (see below)
```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-tf2onnx:1.9.2
```

## after testing pass, tag 
```
docker tag  biop-tf2onnx:1.9.2 biop/biop-tf2onnx:1.9.2
```

## push on dockerhub
```
docker push biop/biop-tf2onnx:1.9.2
```

# Test(s)

## tf2onnx on blob
- train a stardist model
- export using model.export_TF("model_name")
- unzip the model_name.zip to a folder model_name (this folder will contain a "tensorflow_model.pb" file)

- convert the model using tf2onnx, in the terminal :
```
source activate tf2onnx
python -m tf2onnx.convert --saved-model "/path/to/folder/model_name" --output_frozen_graph "/path/to/output/model_name_converted.pb"
```

model_name_converted.pb is the converted model, you can use it in your QuPath script!.

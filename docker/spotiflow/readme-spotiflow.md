

# Latest Version

## build

```
docker build -f spotiflow/Dockerfile-spotiflow  -t biop-spotiflow:v0.6.4 . --no-cache
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind  biop-spotiflow:v0.6.4
```

## after testing pass, tag 
```
docker tag  biop-spotiflow:v0.6.4  biop/biop-spotiflow:v0.6.4 

docker tag  biop-spotiflow:v0.6.4 registry.rcp.epfl.ch/ptbiop/biop-spotiflow:v0.6.4
```

## push on dockerhub
```
docker push biop/biop-spotiflow:v0.6.4
```


# data from OMERO 

https://omero.epfl.ch/webclient/?show=dataset-11228


# TEST 

## within notebook

```python
from spotiflow.model import Spotiflow
from spotiflow.sample_data import test_image_hybiss_2d

# Load sample image
img = test_image_hybiss_2d()
# Or any other image
# img = tifffile.imread("myimage.tif")

# Load a pretrained model
model = Spotiflow.from_pretrained("general")
# Or load your own trained model from folder
# model = Spotiflow.from_folder("./mymodel")

# Predict
points, details = model.predict(img) # points contains the coordinates of the detected spots, the attributes 'heatmap' and 'flow' of `details` contain the predicted full resolution heatmap and the prediction of the stereographic flow respectively (access them by `details.heatmap` or `details.flow`). Retrieved spot intensities are found in `details.intens`.
```

## CLI 

```
conda activate spotiflow
spotiflow-predict /home/biop/2D.tif
```


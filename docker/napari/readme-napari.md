# Latest Version

## build

```
docker build -f napari/Dockerfile-napari  -t biop-napari:0.7.1 .
```

## start to test (see below)

```
docker run -it --rm -p 8888:8888 --gpus device=0  --mount src=D:/,target=/home/biop/local,type=bind biop-napari:0.7.1

```

## after testing pass, tag 
```
docker tag biop-napari:0.7.1 biop/biop-napari:0.7.1
```

## push on dockerhub
```
docker push biop/biop-napari:0.7.1
```

# Test(s)

- [x] Start Napari using icon on the desktop
- [x] Open a sample image
- [x] Start napari from the terminal and check if it works
```
conda activate napari
napari
```

- [x] start napari from a jupyter notebook and check if it works
```
# import sample data
from skimage.data import cells3d

import napari

# create a `Viewer` and `Image` layer here
viewer, image_layer = napari.imshow(cells3d())

# print shape of image data
print(image_layer.data.shape)

# start the event loop and show the viewer
napari.run()
```

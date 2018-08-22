# Neural Style API
Image neural network style transfer API using flask, based on the implementation here:
The algorithm can be used to mix the content of an image with the style of another image. For example, here is a photograph of a door arch rendered in the style of a stained glass painting. 

**Requirement**: Run this project using GPU instance if using FloydHub. CPU instace does not satisfy the RAM requirement.

<p align="center">
    <img src="images/style-images/mosaic.jpg" height="200px">
    <img src="images/content-images/amber.jpg" height="200px">
    <img src="images/output-images/amber-mosaic.jpg" height="440px">
</p>

## Usage
- Run app.py to start flask server
```bash
python app.py
```
- Use the following API call:
```bash
# Template
curl -X POST -o <NAME_&_PATH_DOWNLOADED_IMG> -F "file=@<IMAGE_TO_STYLE>" -F "checkpoint=<MODEL_CHECKPOINT>" <SERVICE_ENDPOINT>

# e.g. of a POST req
curl -X POST -o myfile-udnie.jpg -F "file=@./myfile.jpg" -F "checkpoint=udnie.pth" https://www..floydlabs.com/expose/BhZCFAKom6Z8RptVKskHZW
```

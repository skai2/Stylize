# Neural Style API
Image neural network style transfer API using flask, based on the implementation [here](https://github.com/floydhub/fast-neural-style). 
The algorithm can be used to transfer the artistic style of one image over to another.

**Requirement**: Run this project using GPU instance if using FloydHub. CPU instace does not satisfy the RAM requirement.

## Usage
- Run app.py to start flask server
```bash
python app.py
```
- Use the following API call:
```bash
# Template
curl -X POST -o <NAME_&_PATH_DOWNLOADED_IMG> -F "file=@<IMAGE_TO_STYLE>" -F "checkpoint=<MODEL_CHECKPOINT>" <SERVICE_ENDPOINT>

# e.g. of a POST req using FloydHub
curl -X POST -o myfile-udnie.jpg -F "file=@./myfile.jpg" -F "checkpoint=udnie.pth" https://www..floydlabs.com/expose/BhZCFAKom6Z8RptVKskHZW
```

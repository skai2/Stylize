# Neural Style API
Image neural network style transfer API using flask, based on the implementation [here](https://github.com/lengstrom/fast-style-transfer). 
The algorithm can be used to transfer the artistic style of one image over to another.

## Usage
- Clone project to server and enter directory
```bash
git clone https://github.com/skai2/Stylize.git
```
- Enter project directory
```bash
cd Stylize
```
- Install requirements
```bash
pip install -r requirements.txt
```
- Run app.py to start flask server
```bash
python app.py
```
- Use the following API call:
```bash
# Template
curl -X POST -F "file=@<IMAGE_TO_STYLE>" -F "checkpoint=<MODEL_CHECKPOINT>" <SERVICE_ENDPOINT>

# e.g. of a POST req on a local server
curl -X POST -F "file=@./myfile.jpg" -F "checkpoint=models/udnie.ckpt" https://127.0.0.1:5000/
```
Checkpoint options are:
  - models/udnie.ckpt
  - models/la_muse.ckpt
  - models/rain_princess.ckpt
  - models/scream.ckpt
  - models/wave.ckpt
  - models/wreck.ckpt

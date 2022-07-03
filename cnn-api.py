# References:
# - https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html

import io
import json
import torch
import torch.nn as nn
import torchvision.transforms as transforms

from flask import Flask, jsonify, request
from torchvision import models
from PIL import Image

app = Flask(__name__)
model = models.resnet18(pretrained=True)
model.eval()
imagenet_class_index = json.load(open('assets/imagenet_class_index.json'))
imagenet_class_index = {key: val[1] for key, val in imagenet_class_index.items()}

def preprocess(image_bytes):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])
    ])
    
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    image = transform(image).unsqueeze(0)
    
    return image

def get_prediction(image_bytes):
    tensors = preprocess(image_bytes=image_bytes)
    
    with torch.no_grad():
        outputs = model(tensors)
    prob = nn.Softmax()(outputs[0])
    
    pred_idx  = prob.argmax().item()
    pred_prob = prob[pred_idx].item()
    pred_cls  = imagenet_class_index[str(pred_idx)]
    
    return {'class_id': pred_idx, 'class_name': pred_cls, 'probability': pred_prob}

@app.route('/')
def home():
    return 'CNN API with Pytorch & Flask. We use pretrained resnet18 to classify images.'

@app.route('/predict', methods=['POST'])
def predict():
    if request.method != 'POST':
        return
    if 'image_bytes' not in request.files:
        return 'Error code: 400. Bad Request! image_bytes tidak ditemukan', 400
    image_bytes = request.files['image_bytes']
    image_bytes = image_bytes.read()
    result      = get_prediction(image_bytes)
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)
# References
# - https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
# - https://stackoverflow.com/questions/47198948/convert-bytes-into-bufferedreader-in-python
# - https://stackoverflow.com/questions/33101935/convert-pil-image-to-byte-array

import io
import json
import pandas as pd
import requests
import streamlit as st
from PIL import Image

st.title("Web App for Classifying Image with Pytorch, Flask, and Streamlit")

uploaded_image = st.file_uploader('Upload your image here ...', type=['png', 'jpeg', 'jpg'])
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded image.', use_column_width='auto')
    
    with st.spinner('Classifying the image. It may take a while. Please wait ...'):
        image_bytes = io.BytesIO()
        image.save(image_bytes, format=image.format)
        image_bytes = image_bytes.getvalue()
        response = requests.post("http://127.0.0.1:5000/predict",
                                files={'image_bytes': image_bytes})
    
    st.success("Classification success!")
    
    result = json.loads(response.text)
    st.table(pd.DataFrame({
        'Class ID'   : [result['class_id']],
        'Class Name' : [result['class_name']],
        'Probability': [f"{100*result['probability']:.2f}%"],
    }))
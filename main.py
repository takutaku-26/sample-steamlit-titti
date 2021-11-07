import streamlit as st
from PIL import Image
import requests
import io
from PIL import ImageDraw

st.title('顔認証アプリ')
subscription_key = "3a6c3cc360f94e47a76ab6b3f7be6068"
assert subscription_key
face_api_url= 'https://20211106takutaku.cognitiveservices.azure.com/face/v1.0/detect'

uploaded_file = st.file_uploader("Choose an image...", type='jpg')

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    with io.BytesIO() as output:
        img.save(output, format='JPEG')
        bainary_img = output.getvalue()
    headers = {
    'Content-Type' : 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key}

    params = {
        'returnFaceId': 'true',
        'returnfaceattributes':'age,gender'
    }
    res = requests.post(face_api_url, params=params, headers=headers, data=bainary_img)

    results = res.json()
    for result in results:
        rect = result['faceRectangle']
        draw = ImageDraw.Draw(img)
        draw.rectangle([(rect['left'], rect['top']), (rect['left']+rect['width'],rect['top']+rect['height'])], fill=None, outline='green', width=5)

    st.image(img, caption="Uploaded Image.", use_column_width=True)
    #img = Image.open("キャプチャ.JPG")

    #img.show(img)


    #with open('キャプチャ.JPG', 'rb') as f:
    #    bainary_img = f.read()


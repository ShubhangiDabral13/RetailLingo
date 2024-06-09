import streamlit as st
from Huggingface_fewshot import get_few_shot_db_chain
from PIL import Image, ImageEnhance, ImageFilter
import base64
from io import BytesIO

# Function to apply Gaussian blur to the image
def blur_image(image, blur_radius=1):
    return image.filter(ImageFilter.GaussianBlur(blur_radius))

# Function to lighten the image
def lighten_image(image_path, brightness_factor=1.0):
    img = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(img)
    lightened_img = enhancer.enhance(brightness_factor)
    return lightened_img

# Function to convert image to base64
def get_base64_from_image(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Function to set background image with blur and lightness adjustment
def set_background(image_path, brightness_factor=0.99, blur_radius=1):
    lightened_img = lighten_image(image_path, brightness_factor)
    blurred_img = blur_image(lightened_img, blur_radius)
    base64_img = get_base64_from_image(blurred_img)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
    }
    </style>
    ''' % base64_img
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Setting the background image
set_background('image/back2.png', brightness_factor=0.99, blur_radius=1)

st.markdown(
    "<h1 style='color: #38413c;'>RetailLingo: Translating Human Words to SQL for Retail Proficiency</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='color: #164B60;font-size: 17px;'>Enter your question below.</p>",
    unsafe_allow_html=True
)


question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)

"""
Module for the Stock Image Generation demo page.

This module provides functionality to generate stock images using Vertex AI's
Imagen model. Users can specify a background, foreground, art style, and aspect
ratio to generate images.
"""

import os
import time
import streamlit as st
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

def generate_stock_images(background, foreground, art_style, aspect_ratio):
    """
    Generates stock images using the Vertex AI Imagen model.

    This function initializes the Vertex AI SDK, constructs a prompt based on the
    provided arguments, and requests image generation from the 'imagen-3.0-generate-001'
    model. Generated images are saved locally to the 'content/stock-image-generation/' directory.

    Args:
        background (str): Description of the background for the image.
        foreground (str): Description of the foreground for the image.
        art_style (str): The desired art style (e.g., "Realistic", "Cartoonish").
        aspect_ratio (str): The aspect ratio of the generated images (e.g., "1:1", "16:9").

    Returns:
        list[str]: A list of file paths to the locally saved generated images.
    """
    vertexai.init(
        project=os.environ["PROJECT_ID"],
        location=os.environ["LOCATION"]
    )
    imagen_model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")

    prompt = f"""
SYSTEM: ```You are an expert in Image Generation. You understeand all the details and create a captivating high resolution images. ```
INSTRUCTIONS: ``` Based on the provided Foreground, Background, and Art Style generate a compelling image. Ensure to keep the image clear and high quality. ```
Background: {background}
Foreground: {foreground}
Art Style: {art_style}
"""

    images = imagen_model.generate_images(
        prompt=prompt,
        number_of_images=4,
        aspect_ratio=aspect_ratio,
        safety_filter_level="block_few",
        person_generation="allow_adult"
    )
    len_of_images = len(os.listdir("content/stock-image-generation/"))
    final_images = []
    for i, image in enumerate(images):
        image.save(f"content/stock-image-generation/{len_of_images+i+1}.png")
        final_images.append(f"content/stock-image-generation/{len_of_images+i+1}.png")
    return final_images




def Stock_Image_Generation():
    """
    Renders the Stock Image Generation demo page.

    This function provides a UI for users to:
    - Input a background description.
    - Input a foreground description.
    - Select an art style.
    - Select an aspect ratio.

    Upon clicking "Generate", it calls `generate_stock_images` (or uses cached images
    for a specific hardcoded demo case) and displays the results.

    Returns:
        None
    """
    st.header("Story Image Generation")

    background = st.text_input("Describe the Background...", "A white background with a small flower pot on the right bottom corner")
    foreground = st.text_input("Describe the Foreground...", "An Indian girl in her 20s wearing a floral top and blue jeans standing")
    art_style = st.selectbox("Select Art Style...", options=[
        "Realistic",
        "Realism",
        "Photorealism",
        "Photorealistic",
        "Cartoonish",
        "Painterly",
        "Sketchy",
        "Abstract"
    ])
    aspect_ratio = st.selectbox("Select Aspect Ratio...", options=["1:1", "9:16", "16:9", "4:3", "3:4"], index=2)

    if st.button("Generate"):
        with st.spinner("Generating the Stock Photos..."):
            if background == "A white background with a small flower pot on the right bottom corner" and foreground == "An Indian girl in her 20s wearing a floral top and blue jeans standing":
                time.sleep(5)
                images = ["./content/cached-images/1.png", "./content/cached-images/2.png", "./content/cached-images/3.png", "./content/cached-images/4.png"]
            else:
                images = generate_stock_images(background, foreground, art_style, aspect_ratio)
        with st.expander("Click here to view the generated stock photos..."):
            col1, col2 = st.columns(2)
            for i, image in enumerate(images):
                if i % 2 == 0:
                    col1.image(image)
                else:
                    col2.image(image)

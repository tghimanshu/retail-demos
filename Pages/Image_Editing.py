"""
Module for the Image Editing demo page.

This module allows users to select from various image editing use cases
(e.g., In-painting, Out-painting, Background Change) and view the corresponding
input and output images.
"""

import streamlit as st
import time
import os

def Image_Editing():
    """
    Renders the Image Editing demo page.

    This function:
    1. Displays a header.
    2. Provides a dropdown to select a specific use case (e.g., "Floral Lady In Painting Remove").
    3. Upon clicking "Generate":
        - Displays the input image for the selected use case.
        - Simulates a processing delay.
        - Displays the pre-generated output images from the file system.

    Returns:
        None
    """
    st.header("Image Editing")

    use_cases = [
        "Floral Lady In Painting Remove",
        "Floral Lady In Painting Remove v2",
        "Floral Lady Out Painting",
        "Floral Lady Change Background",
        "In Painting Insert",
        "In Painting Remove",
        "Out Painting",
        "Out Painting and Background Change",
        "In Painting User Pan",
        "In Painting User MakeUp",
    ]

    use_case = st.selectbox("Select a use case...", use_cases)

    if st.button("Generate"):
        if not use_case:
            st.error("Please select a use case.")
        else:
            st.write("Selected Use Case:", use_case)
            use_case_parsed = '-'.join(use_case.lower().split(' '))
            with st.expander("Click here to view the Input image..."):
                col1, _ = st.columns(2)
                col1.image(f"content/image-editing/{use_case_parsed}.png")
            with st.spinner("Generating the Customized Images..."):
                time.sleep(2)
            with st.expander("Click here to view the Customized Images..."):
                c1, c2 = st.columns(2)
                for i in range(len(os.listdir(f"content/image-editing/{use_case_parsed}"))):
                    if i % 2 == 0:
                        c1.image(f"content/image-editing/{use_case_parsed}/img{i+1}.png")
                    else:
                        c2.image(f"content/image-editing/{use_case_parsed}/img{i+1}.png")

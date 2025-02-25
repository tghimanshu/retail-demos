import streamlit as st
import time
import os

def Video_Generation():
    st.header("Video Generation")

    use_cases = [
        "Women Wear",
        "Men Wear",
        "Bag",
        "Home Decor",
        "Jewellery",
    ]

    use_case = st.selectbox("Select a use case...", use_cases)

    if st.button("Generate"):
        if not use_case:
            st.error("Please select a use case.")
        else:
            st.write("Selected Use Case:", use_case)
            use_case_parsed = 'meesho-' + '-'.join(use_case.lower().split(' '))
            with st.expander("Click here to view the Input image..."):
                col1, _ = st.columns(2)
                col1.image(f"content/video-generation/{use_case_parsed}.png")
            with st.spinner("Generating the Video"):
                time.sleep(2)
            with st.expander("Click here to view the Generated Videos..."):
                c1, c2 = st.columns(2)
                for i in range(len(os.listdir(f"content/video-generation/output/{use_case_parsed}"))):
                    if i % 2 == 0:
                        c1.video(f"content/video-generation/output/{use_case_parsed}/{use_case_parsed}-{i}.mp4")
                    else:
                        c2.video(f"content/video-generation/output/{use_case_parsed}/{use_case_parsed}-{i}.mp4")



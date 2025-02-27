import streamlit as st

def Home():
    st.image("./content/logos/genai-live-poster.jpg", use_container_width=True)
    st.write(f"# Welcome to GenAI Live!")
    st.write("Powered by")
    st.image("./content/logos/gemini-logo.png", width=80)

    st.divider()

    st.write("""
**Welcome to our Gemini Powered Content Creation**

Dive into the world of Content Creation with Google.

**What you can expect:**

* **Video Generation:** Witness the power of AI in creating captivating motion videos using Veo 2, to add life to product pictures
* **Stock Image Generation:** Explore how AI can create stock photos for multiple categories and scenarios for landing/home pages
* **Image Editing:** Edit image background for seller and user created images. Images which are cut, are fixed by AI. Increase conversion through superior images

**Let's increase customer engagement and conversion with you!**
""")
# Vertex Vision Demos

This repository contains a Streamlit-based application showcasing various computer vision and generative AI demos powered by Google Cloud Vertex AI and Gemini.

## Table of Contents
- [Overview](#overview)
- [Demos](#demos)
  - [Video Generation](#video-generation)
  - [Stock Image Generation](#stock-image-generation)
  - [Image Editing](#image-editing)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contact](#contact)

## Overview

The **Vertex Vision Demos** application serves as a platform to demonstrate the capabilities of generative AI models in creating and editing media content. It is designed to show how these technologies can enhance content creation workflows, increase customer engagement, and improve conversion rates.

## Demos

The application includes the following interactive demos:

### Video Generation
Witness the power of AI in creating captivating motion videos using Veo 2 (or similar models) to add life to product pictures. This demo allows users to select from various use cases (e.g., "Dining Area", "Room", "Sofa") and view generated videos based on input images.

### Stock Image Generation
Explore how AI can create stock photos for multiple categories and scenarios for landing/home pages. Users can specify a background, foreground, art style, and aspect ratio to generate high-quality images using Vertex AI's Imagen model.

### Image Editing
Edit image backgrounds for seller and user-created images. This demo showcases capabilities like In-painting, Out-painting, and background replacement to fix or enhance images.

## Prerequisites

- **Python 3.8+**
- **Google Cloud Platform (GCP) Project** with Vertex AI API enabled.
- **Vertex AI SDK** credentials configured.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone git@gitlab.com:google-cloud-ce/googlers/himanshukgohil/vertex-vision-demos.git
    cd vertex-vision-demos
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**
    You need to set the `PROJECT_ID` and `LOCATION` environment variables for the Vertex AI integration to work.

    ```bash
    export PROJECT_ID=[Your Project ID]
    export LOCATION=[Your Region]
    ```

## Usage

1.  **Run the Streamlit application:**
    ```bash
    streamlit run Home.py
    ```

2.  **Access the App:**
    Open your web browser and navigate to the URL displayed in the terminal (usually `http://localhost:8501`).

3.  **Navigate Demos:**
    Use the sidebar menu to switch between the Home page and different demos (Stock Image Generation, Image Editing, Video Generation).

## Project Structure

```
vertex-vision-demos/
├── .streamlit/                 # Streamlit configuration
├── content/                    # Static content (images, logos, cached outputs)
├── Pages/                      # Source code for individual demo pages
│   ├── Home.py                 # Home page logic
│   ├── Image_Editing.py        # Image Editing demo logic
│   ├── Image_Generation.py     # Image Generation placeholder
│   ├── Stock_Image_Generation.py # Stock Image Generation logic
│   └── Video_Generation.py     # Video Generation demo logic
├── Home.py                     # Main application entry point
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
└── deploy.sh                   # Deployment script
```

## Contact

For any questions or feedback, please contact [himanshukgohil@google.com].

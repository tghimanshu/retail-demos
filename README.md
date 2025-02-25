# Vertex Vision Demos

This repository contains various demos and examples related to Meesho's technology and services.

## Contents

-   **[Demo 1 Name]**: Video Generation
-   **[Demo 2 Name]**: Stock Image Generation
-   **[Demo 3 Name]**: Image Editing

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone git@gitlab.com:google-cloud-ce/googlers/himanshukgohil/vertex-vision-demos.git
    ```
2.  **Navigate to the demo directory:**
    ```bash
    cd vertex-vision-demos
    ```
3. **Create a virtual environment (optional):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4. **Install required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5. **Update Environment Variables:**
    ```bash
    export PROJECT=[Your Project ID]
    export LOCATION=[Your Region]
    ```
6. **Run the App Locally**
    ```bash
    streamlit run Home.py
    ```
7. **To Deploy on your GCP Account update the deploy.sh file with your project details**
    ```bash
    source deploy.sh
    ```

## Contact

For any questions or feedback, please contact [himanshukgohil@google.com].

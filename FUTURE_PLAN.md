# Future Plan (Phase 2)

This document outlines the proposed enhancements and features for the next phase of the Vertex Vision Demos project. Phase 1 focused on establishing the core infrastructure and initial set of demos. Phase 2 aims to expand functionality, improve user experience, and integrate more advanced AI capabilities.

## 1. Feature Enhancements

### 1.1. Advanced Image Generation
-   **Implementation in `Pages/Image_Generation.py`**: The current placeholder should be fully implemented.
-   **Capabilities**: Add support for more granular control over image generation parameters (e.g., negative prompts, seed selection, guidance scale).
-   **Model Upgrades**: Integrate newer versions of Imagen models as they become available.

### 1.2. Enhanced Image Editing
-   **Interactive Canvas**: Replace the static dropdown selection with an interactive canvas where users can draw masks for in-painting and out-painting directly on the uploaded image.
-   **User Uploads**: Allow users to upload their own images for editing, rather than relying solely on pre-defined use cases.

### 1.3. Real-time Video Generation
-   **Dynamic Inputs**: Move beyond pre-generated video outputs. Allow users to upload an image and generate a video in real-time (or near real-time, depending on API latency).
-   **Prompt Control**: Add text-to-video capabilities where users can describe the desired motion or scene transformation.

## 2. Infrastructure & Architecture

### 2.1. Caching & Performance
-   **Result Caching**: Implement more robust caching mechanisms for API calls to reduce latency and costs for repeated requests.
-   **Async Processing**: Use asynchronous calls for long-running generation tasks to prevent blocking the Streamlit UI.

### 2.2. Error Handling & Logging
-   **Robust Error Handling**: specific error handling for Vertex AI API quotas, network issues, and invalid inputs.
-   **Logging**: Implement structured logging to track usage patterns and debug issues more effectively.

### 2.3. Modularization
-   **Utils Package**: Create a `utils` package to house shared helper functions (e.g., UI components, API wrappers) to reduce code duplication across pages.
-   **Configuration**: Move hardcoded values (like model names and prompt templates) into a centralized configuration file.

## 3. UI/UX Improvements

### 3.1. Responsive Design
-   Ensure the application layout adapts gracefully to different screen sizes and devices.

### 3.2. User Feedback
-   Add mechanisms for users to rate generated content or provide feedback, which can be used for future model tuning or prompt engineering improvements.

## 4. Testing & CI/CD

### 4.1. Unit Tests
-   Add unit tests for helper functions and core logic.

### 4.2. Integration Tests
-   Implement integration tests to verify the end-to-end flow with Vertex AI APIs (using mocks where appropriate to save costs).

### 4.3. Automated Deployment
-   Enhance `deploy.sh` or set up a CI/CD pipeline (e.g., Cloud Build, GitHub Actions) to automate testing and deployment to Cloud Run or App Engine.

# 🌿 AI Plant Disease Detection System

📸 
if you want to see video for this project i posted a video on my Linkedin
 link: https://www.linkedin.com/posts/abdelrahman-abdelghany-302a532a3_deeplearning-computervision-tensorflow-activity-7480879685367754754-qmmM?utm_source=share&utm_medium=member_desktop&rcm=ACoAAElN0vIBJ8V3GwZxoJp_3zDnNnKBoYQduSQ



An end-to-end Computer Vision system designed to automatically classify plant species and diagnose crop diseases from leaf images. The system accepts leaf photos, detects the specific disease (or confirms if the plant is healthy), and outputs real-time confidence scores.

## 💡 Project Overview & Business Value
In the realm of Computer Vision, many solutions rely on extremely heavy, pre-trained architectures (like ResNet or VGG) that demand massive computational power and GPU-backed hosting. 

This project takes a pragmatic, highly optimized approach. It is an end-to-end deep learning system built from scratch to detect plant diseases from leaf images with exceptional accuracy and minimal resource consumption.

**Why this approach?**
* **Ultra-Lightweight Architecture:** By utilizing smart architectural decisions (such as `GlobalAveragePooling2D` instead of massive `Flatten` layers), the final compiled model weighs in at **under 800 KB**. This makes it incredibly fast to load and highly deployable on low-end cloud instances or edge devices.
* **High Precision & Robustness:** Achieved a **~95.5% real-world accuracy**. By strictly implementing Batch Normalization and Dropout layers, the model is immune to overfitting and generalizes perfectly to unseen, real-world field conditions.
* **Cost-Effective Agritech Solution:** Provides a scalable, instant diagnostic tool for farmers, agricultural engineers, and startups. It eliminates the need for expensive infrastructure while delivering instantaneous, reliable results to prevent crop loss.

## 🛠️ Tech Stack & Architecture
The project features a decoupled, production-ready architecture:

* **Core Deep Learning (Model):** Python, TensorFlow & Keras (Custom CNN Architecture, TF Data Pipelines with Caching & Prefetching for optimized hardware utilization).
* **Backend API (Inference Engine):** FastAPI and Uvicorn. Serves the model efficiently and handles asynchronous image processing requests.
* **Web UI (Frontend):** Streamlit. Provides a clean, responsive, and user-friendly web dashboard for seamless interaction.
* **Dataset:** Trained on the robust **PlantVillage Dataset** (Color images).

## 🚀 Key Features
* **Dual-Tier System:** A clean separation of concerns. The `api.py` acts as a microservice processing the heavy lifting, while `Front.py` handles user experience, making the system highly scalable.
* **Batch Processing:** Capable of analyzing and inferring multiple leaf images simultaneously with real-time confidence scores.
* **Instant Inference:** Delivers sub-second response times thanks to the lightweight CNN backbone.


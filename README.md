# 🛍️ AI-Driven Fashion Image Classifier

A robust and scalable solution for automating product categorization in the fashion retail industry. This project demonstrates the use of AI-powered image classification to enhance customer experience and streamline inventory management.

[**Try the Live App Here!**](https://fashion-image-classifier.streamlit.app/)

---

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Technology Stack](#technology-stack)
4. [How It Works](#how-it-works)
5. [Results](#results)
6. [Setup Instructions](#setup-instructions)
7. [Future Work](#future-work)
8. [License](#license)

---

## 📖 Project Overview

FashionTrend, a leading online fashion retailer, faces challenges managing a growing and diverse product catalog. This project addresses the problem by using AI to automate product categorization, enhancing search, filtering, and inventory management.

This repository includes:
- AI models (CNN and MobileNetV2) trained for multi-label classification of fashion images.
- A user-friendly **Streamlit app** deployed via Docker for interactive demonstrations.

---

## ✨ Key Features

- **Multi-Label Classification**: Categorizes products by `masterCategory` (e.g., Apparel, Accessories) and `Gender`.
- **Two AI Models**:
  - CNN (79% Accuracy)
  - MobileNetV2 (84% Accuracy)
- **Interactive App**:
  - Single Image Prediction
  - Multiple Image Upload
  - Batch Image Prediction via Zip Files
- **Deployed Live**: Accessible via [Streamlit](https://fashion-image-classifier.streamlit.app/).

---

## 🛠️ Technology Stack

- **Deep Learning Framework**: TensorFlow/Keras
- **Frontend**: Streamlit
- **Deployment**: Docker
- **Programming Language**: Python
- **Data Preprocessing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn

---

## 🔍 How It Works

### 1. **Data Preprocessing**
   - Images resized to `128x128 pixels`.
   - Normalization applied for consistent scaling.
   - Augmentation techniques like rotation, zoom, and flipping to improve model generalization.

### 2. **Model Training**
   - **CNN**: Custom-built model for accuracy and simplicity.
   - **MobileNetV2**: Pretrained model optimized for lightweight deployment.
   - Dataset split: 80% training, 20% validation.

### 3. **Deployment**
   - Built an interactive web app using **Streamlit**.
   - Deployed via Docker for scalability and portability.

---

## 📊 Results

| Model         | Accuracy | Key Features                        |
|---------------|----------|--------------------------------------|
| CNN           | 79%      | Lightweight, simple architecture    |
| MobileNetV2   | 84%      | Pretrained, optimized for scalability |

![Streamlit App Interface](https://placehold.co/800x400?text=Streamlit+App+Interface+Screenshot)

**Live Demo**: [https://fashion-image-classifier.streamlit.app/](https://fashion-image-classifier.streamlit.app/)

---

## 🛠️ Setup Instructions

Follow these steps to set up the project locally:

### Prerequisites
- Python 3.9 or higher
- Docker installed

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bopitien/AI-Driven-Image-Classification-for-Fashion-Retailer

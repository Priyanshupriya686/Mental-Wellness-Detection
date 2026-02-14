# 🧠 Mental Wellness Detection System

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-2.0+-green.svg" alt="Flask Version">
  <img src="https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange.svg" alt="ML Algorithm">
  <img src="https://img.shields.io/badge/NLP-Text%20Analysis-purple.svg" alt="NLP">
  <img src="https://img.shields.io/badge/API-Reddit%20%7C%20Twitter-red.svg" alt="APIs">
  <img src="https://img.shields.io/badge/Deployment-ngrok-yellow.svg" alt="Deployment">
</div>

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Objectives](#-objectives)
- [Key Features](#-key-features)
- [Theoretical Foundation: WEMWBS-Based Wellness Scoring](#-theoretical-foundation-wemwbs-based-wellness-scoring)
- [Feature Engineering & ML Pipeline](#-feature-engineering--ml-pipeline)
- [Flask + ngrok Web Interface](#-flask--ngrok-web-interface)
- [Quick Start Guide](#-quick-start-guide)
- [Sample Output](#-sample-output)
- [Future Enhancements](#-future-enhancements)
- [Technologies & Libraries](#-technologies--libraries)
- [Model Performance](#-model-performance)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)
- [Contributors](#-contributors)

---

## 🌟 Overview

Welcome to the **Mental Wellness Detection System** – an innovative AI-powered platform that transforms social media insights into personalized mental wellness assessments. By analyzing linguistic and behavioral patterns from Reddit and X (Twitter) posts, our system provides a comprehensive wellness score inspired by the Warwick–Edinburgh Mental Well-being Scale (WEMWBS).

Imagine a world where your social media activity becomes a mirror to your inner well-being. Our system bridges the gap between digital footprints and mental health awareness, offering real-time, data-driven insights through an intuitive web interface.



---

## 🎯 Objectives

- **🔍 Evaluate Mental Wellness**: Harness linguistic and behavioral cues from social media to assess psychological well-being
- **🧠 AI-Driven Insights**: Develop a sophisticated model based on WEMWBS-inspired positive psychology principles
- **🌐 Real-Time Integration**: Seamlessly connect machine learning with live social media APIs
- **💡 Accessible Awareness**: Create a user-friendly web tool to promote mental health consciousness through technology

---

## ✨ Key Features

<div align="center">

| Feature | Description | Status |
|---------|-------------|--------|
| 📊 **Dataset-Driven Model** | Trained on authentic mental health survey data | ✅ Complete |
| 🏆 **WEMWBS-Inspired Scoring** | Wellness score (0-100) reflecting positive mental health indicators | ✅ Complete |
| 🌲 **Random Forest Classifier** | Advanced ML algorithm for depression level prediction | ✅ Complete |
| 🔄 **Real-Time API Integration** | Live data fetching from Reddit (PRAW) and X/Twitter (Tweepy) | ✅ Complete |
| 🌐 **Flask Web Interface** | Interactive web app with ngrok deployment for public access | ✅ Complete |
| 📋 **Personalized Reports** | Detailed wellness analysis with actionable improvement suggestions | ✅ Complete |

</div>

---

## 🧬 Theoretical Foundation: WEMWBS-Based Wellness Scoring

The **Warwick–Edinburgh Mental Well-being Scale (WEMWBS)** represents a paradigm shift in mental health assessment – focusing on **positive well-being** rather than pathology.

### 🔹 Our Approach:
- **Wellness Score (0–100)**: Higher scores = greater emotional balance and optimism
- **Positive Psychology Focus**: Measures optimism, relaxation, social connectedness, and clear thinking
- **Research-Backed**: Aligned with established mental health research standards


---

## ⚙️ Feature Engineering & ML Pipeline

### Data Processing:
- **📝 Categorical Encoding**: LabelEncoder transforms survey responses
- **🔢 Normalization**: MinMaxScaler ensures 0-1 feature scaling
- **📊 Wellness Calculation**: Inverse mean of negative indicators for positive scaling

### Wellness Categories:
- 🟢 **High (≥75)**: Excellent mental well-being
- 🟡 **Moderate (≥50)**: Good overall wellness with room for improvement
- 🔴 **Low (<50)**: May indicate mental strain requiring attention

### ML Model:
- **Algorithm**: Random Forest Classifier
- **Training Data**: Social media and mental health survey dataset
- **Evaluation**: Comprehensive metrics (Accuracy, Precision, Recall, F1-Score)

---

## 🌐 Flask + ngrok Web Interface

### 🧱 Interactive Web Application
- **User-Friendly Form**: Simple platform and username input
- **Comprehensive Reports**: Depression level, wellness score, category, and personalized feedback
- **Responsive Design**: Clean, modern UI for optimal user experience

### 🌍 ngrok Deployment
- **Public Access**: Temporary HTTPS tunnel from Colab environment
- **Live Testing**: Shareable link for real-world demonstration
- **Secure Connection**: Encrypted data transmission



---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8+
- Google Colab account (for ngrok deployment)
- Kaggle API token
- Reddit API credentials
- Twitter API credentials

### Installation

```bash
# Clone the repository
git clone https://github.com/your-repo/Mental-Wellness-Detection.git
cd Mental-Wellness-Detection

# Install dependencies
pip install -r requirements.txt

# Alternative: Using Conda
conda env create -f environment.yml
conda activate mental-wellness-detection

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Upload Kaggle credentials
from google.colab import files
files.upload()  # Upload kaggle.json
```

### Data Acquisition

```bash
# Download dataset
kaggle datasets download -d souvikahmed071/social-media-and-mental-health -p /content/data
unzip /content/data/social-media-and-mental-health.zip -d /content/data
```

### Model Training

```python
# Load and preprocess data
# Encode categorical features
# Train Random Forest model
# Evaluate performance
# Generate wellness metrics
```

### Launch Application

```bash
python app.py
```

**🎉 Access your public ngrok URL and start analyzing wellness!**

---

## 📊 Sample Output

```
🌐 Platform: Reddit
👤 Username: example_user
📈 Predicted Depression Level: 2
🎯 Wellness Score: 82 / 100
📊 Category: High
💡 Insight: You are doing great! Keep nurturing positive habits.
```

---

## 🔮 Future Enhancements

<div align="center">

| Enhancement | Description | Priority |
|-------------|-------------|----------|
| 🤖 **Advanced ML Algorithms** | Experiment with XGBoost, SVM, Neural Networks | 🔴 High |
| 📈 **Performance Metrics** | Compare F1, Recall, Precision, Accuracy across models | 🔴 High |
| 🌍 **Multi-Platform Support** | Extend to Instagram, Facebook, LinkedIn | 🟡 Medium |
| 📱 **Mobile App** | Native iOS/Android application | 🟡 Medium |
| 🔒 **Privacy & Ethics** | Enhanced data anonymization and consent mechanisms | 🔴 High |
| 📊 **Longitudinal Tracking** | Historical wellness trend analysis | 🟡 Medium |
| 🔔 **Alert System** | Proactive wellness notifications | 🟢 Low |

</div>

---

## 🛠️ Technologies & Libraries

<div align="center">

| Category | Technologies |
|----------|--------------|
| **Programming** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **Data Science** | ![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) |
| **Web Framework** | ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) |
| **APIs** | ![Reddit](https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white) ![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white) |
| **Deployment** | ![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white) ![Ngrok](https://img.shields.io/badge/Ngrok-1F77B4?style=for-the-badge&logo=ngrok&logoColor=white) |

</div>

---

## 📈 Model Performance

<div align="center">

| Metric | Score |
|--------|-------|
| **Accuracy** | 0.6435 |
| **Precision** | 0.5536 |
| **Recall** | 0.6127 |
| **F1-Score** | 0.6358 |

</div>

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Warwick–Edinburgh Mental Well-being Scale (WEMWBS)** researchers
- **Kaggle** for the mental health dataset
- **Open-source community** for amazing libraries and tools

---

<div align="center">

**Made with ❤️ for mental health awareness**

⭐ **Star this repo if you find it helpful!**

[🔗 Live Demo](https://your-ngrok-link-here) | [📧 Contact](mailto:your-email@example.com) | [🐛 Report Issues](https://github.com/your-repo/issues)

</div>

---

---

## 👥 Contributors

Thanks to all the wonderful people who have contributed to this project!

<a href="https://github.com/Priyanshupriya686/Mental-Wellness-Detection/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Priyanshupriya686/Mental-Wellness-Detection" />
</a>

---

<div align="center">
  <img src="https://img.shields.io/github/stars/your-repo?style=social" alt="GitHub Stars">
  <img src="https://img.shields.io/github/forks/your-repo?style=social" alt="GitHub Forks">
  <img src="https://img.shields.io/github/watchers/your-repo?style=social" alt="GitHub Watchers">
</div>

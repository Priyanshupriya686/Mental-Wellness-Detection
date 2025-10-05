🧠 Mental Wellness Detection System
🔍 A Machine Learning & NLP-based project that predicts an individual's mental wellness level using social media posts.


🚀 Overview

This project analyzes users’ social media posts (Reddit or X/Twitter) to assess their mental wellness level.
It combines data-driven machine learning analysis with real-time social media integration using APIs.
The web interface (built with Flask & ngrok) allows anyone to input a username and receive a wellness report containing a  wellness score, and categorized insights.

The wellness scoring framework is inspired by the Warwick–Edinburgh Mental Well-being Scale (WEMWBS), which measures positive mental health through self-perception indicators like optimism, clarity of thought, energy, and social connectedness.


🎯 Objectives

To evaluate mental wellness using linguistic and behavioral cues from social media activity.

To design an AI model based on the WEMWBS scoring philosophy.

To integrate machine learning and NLP with real-world social media APIs.

To provide an accessible web-based tool demonstrating the use of AI in mental health awareness.

🧩 Key Features

✅ Dataset-based model trained on real mental health survey data
✅ Wellness score mapped to WEMWBS-inspired positive psychology indicators
✅ Random Forest Classifier for depression-level prediction
✅ Real-time API integration with Reddit and X (Twitter)
✅ Flask + ngrok web interface for public testing
✅ Personalized Wellness Report with improvement suggestions

🧠 Technologies & Libraries Used
Category	Tools / Libraries
Programming Language	Python
Data Handling	Pandas, NumPy
Web Framework	Flask
API Integration	PRAW (Reddit), Tweepy (X/Twitter)
Deployment (Colab)	Pyngrok


🧬 Theoretical Foundation: WEMWBS-Based Wellness Scoring

The Warwick–Edinburgh Mental Well-being Scale (WEMWBS) is a standardized tool developed by researchers at the Universities of Warwick and Edinburgh.
It measures positive aspects of mental health rather than mental illness — focusing on optimism, relaxation, social connectedness, and clear thinking.

🔹 In this project:

Project’s Wellness Score (0–100) is designed inspired by WEMWBS, where:

Higher scores indicate greater well-being and emotional balance

Lower scores reflect possible mental strain, low optimism, or distress

While your project doesn’t directly administer the WEMWBS questionnaire, it translates behavioral and linguistic cues (from dataset responses and social media posts) into a similar scaled wellness score for interpretability and consistency with mental health research standards.


⚙️ Feature Engineering

Dataset includes questions about attention, restlessness, comparison habits, sleep, and emotional state.

Each categorical response encoded via LabelEncoder.

A MinMaxScaler normalizes data (0–1 range).

The Wellness Score (0–100) is calculated using the inverse mean of negative indicators, following WEMWBS-inspired positive scaling.

Categorization:

High (≥75)

Moderate (≥50)

Low (<50)



🌐 Flask + ngrok Web Interface
🧱 Flask Web App

Interactive form for platform and username input.

Displays:

Depression Level

Wellness Score (WEMWBS-scaled)

Category

Personalized feedback

🌍 ngrok Integration

Used for exposing the Flask server from Colab.

Provides a temporary public HTTPS link for live testing.

🛠️ How to Run the Project
Step 1: Install Dependencies
!pip install pandas numpy scikit-learn flask flask-ngrok pyngrok praw tweepy

Step 2: Mount Drive & Upload Kaggle Token
from google.colab import drive
drive.mount('/content/drive')
from google.colab import files
files.upload()  # Upload kaggle.json

Step 3: Download Dataset
!kaggle datasets download -d souvikahmed071/social-media-and-mental-health -p /content/data
!unzip /content/data/social-media-and-mental-health.zip -d /content/data

Step 4: Train the ML Model

Encodes, trains, evaluates, and generates wellness metrics.

Step 5: Run Flask + ngrok App
!python app.py


Access the ngrok public URL → enter username → view the Wellness Report.

📊 Sample Output
Platform: Reddit  
Username: example_user  
Predicted Depression Level: 2  
Wellness Score: 82 / 100  
Category: High  
✅ You are doing great! Keep positive habits.



🔮 Future Improvements
1. Try few other ML algorithms other than Random Forests and compare on F1, Recall, Precision and Accuracy score

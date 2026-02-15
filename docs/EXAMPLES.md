# 📸 Examples & Sample Outputs

This document contains comprehensive examples and sample outputs from the Mental Wellness Detection system.

---

## Table of Contents
- [Web Interface Screenshots](#web-interface-screenshots)
- [Command Line Examples](#command-line-examples)
- [Sample JSON Responses](#sample-json-responses)
- [Model Training Output](#model-training-output)
- [Batch Processing Example](#batch-processing-example)
- [Evaluation Reports](#evaluation-reports)

---

## Web Interface Screenshots

### Landing Page
```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│        🧠 Mental Wellness Detection System                  │
│                                                             │
│   Analyze your mental well-being through your social       │
│   media activity. Get personalized wellness scores &       │
│   actionable insights.                                      │
│                                                             │
│   ┌─────────────────────────────────────────────────┐      │
│   │                                                 │      │
│   │  Choose Platform:                              │      │
│   │  ○ Reddit     ○ Twitter      ○ Direct Input   │      │
│   │                                                 │      │
│   │  Username/Text: [___________________________]   │      │
│   │                                                 │      │
│   │            [Analyze Wellness]                  │      │
│   │                                                 │      │
│   └─────────────────────────────────────────────────┘      │
│                                                             │
│   ⚠️ Crisis Support: 988 Suicide & Crisis Lifeline        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Results Page
```
┌─────────────────────────────────────────────────────────────┐
│  Mental Wellness Analysis - Results                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Platform: Reddit                                           │
│  Username: positive_thinker                                │
│  Analysis Date: 2025-10-31                                 │
│                                                             │
├─ WELLNESS REPORT ────────────────────────────────────────┤
│                                                             │
│  🎯 Depression Level: 1/5  [Minimal]                       │
│  📊 Wellness Score: 82/100  [HIGH]                         │
│                                                             │
│  Category: 🟢 HIGH WELLNESS                                 │
│  Confidence: 89%                                            │
│                                                             │
├─ KEY INSIGHTS ────────────────────────────────────────────┤
│                                                             │
│  ✅ Positive Indicators:                                    │
│     • Optimistic tone detected                              │
│     • Frequent expressions of gratitude                    │
│     • Strong social engagement                             │
│                                                             │
│  💡 Recommendations:                                        │
│     • Continue current positive habits                     │
│     • Share wellness tips with your community              │
│     • Maintain social connections                          │
│                                                             │
│  📈 Trend: Score improving over past month                 │
│                                                             │
├─ DISCLAIMER ──────────────────────────────────────────────┤
│  This analysis is for awareness only. If experiencing     │
│  mental health crisis, contact: 988 or 1-800-273-8255     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Command Line Examples

### Example 1: Positive Text Analysis

**Command:**
```bash
$ python scripts/predict.py --model models/wellness_model_20251031_074843.joblib \
  --input "I'm feeling amazing today! My life is full of possibilities and I'm grateful for my friends."
```

**Output:**
```
╔════════════════════════════════════════════════════════════╗
║          Mental Wellness Prediction Results               ║
╚════════════════════════════════════════════════════════════╝

📝 Input Text:
"I'm feeling amazing today! My life is full of possibilities 
and I'm grateful for my friends."

─────────────────────────────────────────────────────────────

🎯 RESULTS:

   Depression Level: 1
   Wellness Score: 87 / 100
   Category: HIGH
   Confidence: 0.91

─────────────────────────────────────────────────────────────

💡 KEY INSIGHTS:

   ✅ Sentiment: Positive
   ✅ Emotional Indicators: Gratitude, Optimism
   ✅ Social Connection: Strong
   
   Recommendation: You're in great shape! Keep up these 
                   positive habits and continue nurturing 
                   meaningful relationships.

═══════════════════════════════════════════════════════════════
```

### Example 2: Negative Text Analysis

**Command:**
```bash
$ python scripts/predict.py --model models/wellness_model_20251031_074843.joblib \
  --input "Everything feels hopeless. I can't sleep and nothing makes me happy anymore."
```

**Output:**
```
╔════════════════════════════════════════════════════════════╗
║          Mental Wellness Prediction Results               ║
╚════════════════════════════════════════════════════════════╝

📝 Input Text:
"Everything feels hopeless. I can't sleep and nothing makes 
me happy anymore."

─────────────────────────────────────────────────────────────

🎯 RESULTS:

   Depression Level: 4
   Wellness Score: 32 / 100
   Category: LOW
   Confidence: 0.87

─────────────────────────────────────────────────────────────

⚠️  KEY CONCERNS:

   🔴 Sentiment: Negative
   🔴 Emotional Indicators: Hopelessness, Anhedonia
   🔴 Sleep Issues Detected
   
   🆘 IMMEDIATE RECOMMENDATION:
   
   Your wellness score suggests you may benefit from 
   professional support. Please consider:
   
   • Contacting a mental health professional
   • Reaching out to trusted friends or family
   • 24/7 Crisis Hotline: 988 (US)
   • Crisis Text Line: Text HOME to 741741
   
   You're not alone. Help is available.

═══════════════════════════════════════════════════════════════
```

### Example 3: Neutral Text Analysis

**Command:**
```bash
$ python scripts/predict.py --model models/wellness_model_20251031_074843.joblib \
  --input "Had a regular day at work. Had coffee and lunch with colleagues."
```

**Output:**
```
╔════════════════════════════════════════════════════════════╗
║          Mental Wellness Prediction Results               ║
╚════════════════════════════════════════════════════════════╝

📝 Input Text:
"Had a regular day at work. Had coffee and lunch with 
colleagues."

─────────────────────────────────────────────────────────────

🎯 RESULTS:

   Depression Level: 2
   Wellness Score: 65 / 100
   Category: MODERATE
   Confidence: 0.85

─────────────────────────────────────────────────────────────

💡 INSIGHTS:

   ➖ Sentiment: Neutral
   ➖ Emotional Indicators: Routine, Social Interaction
   ➖ Stability: Stable baseline
   
   Recommendation: You're maintaining a stable wellness 
                   level. Consider adding more activities 
                   that bring you joy or purpose to boost 
                   your wellness score.

═══════════════════════════════════════════════════════════════
```

---

## Sample JSON Responses

### Single Prediction Response

```json
{
  "success": true,
  "timestamp": "2025-10-31T14:30:45Z",
  "input": {
    "text": "Feeling grateful and optimistic about the future!",
    "platform": "direct_input",
    "source": "user_submission"
  },
  "prediction": {
    "depression_level": 1,
    "depression_level_label": "Minimal",
    "wellness_score": 86,
    "category": "HIGH",
    "confidence": 0.92,
    "raw_probabilities": {
      "depression_level_1": 0.92,
      "depression_level_2": 0.05,
      "depression_level_3": 0.02,
      "depression_level_4": 0.01,
      "depression_level_5": 0.00
    }
  },
  "analysis": {
    "positive_indicators": [
      "grateful",
      "optimistic",
      "future_focused",
      "positive_sentiment"
    ],
    "negative_indicators": [],
    "emotional_tone": "positive",
    "sentiment_score": 0.87,
    "social_connection_indicators": [
      "mentions_of_relationships",
      "inclusive_language"
    ]
  },
  "insights": {
    "summary": "Your wellness indicators are excellent. You're displaying positive emotional patterns and optimistic outlook.",
    "category_description": "High wellness - Excellent mental well-being",
    "recommendations": [
      "Continue nurturing positive habits",
      "Share your positive energy with others",
      "Maintain current social connections"
    ],
    "wellness_trajectory": "stable_high"
  },
  "disclaimer": "This analysis is for informational purposes only and not a medical diagnosis."
}
```

### Batch Prediction Response

```json
{
  "success": true,
  "batch_id": "batch_20251031_143045",
  "timestamp": "2025-10-31T14:30:45Z",
  "total_records_processed": 3,
  "results": [
    {
      "record_id": 1,
      "input_text": "Feeling amazing!",
      "wellness_score": 88,
      "category": "HIGH",
      "depression_level": 1,
      "confidence": 0.94
    },
    {
      "record_id": 2,
      "input_text": "Having a rough day",
      "wellness_score": 52,
      "category": "MODERATE",
      "depression_level": 2,
      "confidence": 0.83
    },
    {
      "record_id": 3,
      "input_text": "Struggling with anxiety",
      "wellness_score": 38,
      "category": "LOW",
      "depression_level": 4,
      "confidence": 0.88
    }
  ],
  "summary_statistics": {
    "average_wellness_score": 59.3,
    "high_category_count": 1,
    "moderate_category_count": 1,
    "low_category_count": 1,
    "average_depression_level": 2.3,
    "average_confidence": 0.88
  }
}
```

### Reddit User Analysis Response

```json
{
  "success": true,
  "platform": "reddit",
  "user_analysis": {
    "username": "wellness_advocate",
    "posts_analyzed": 25,
    "analysis_date": "2025-10-31",
    "overall_wellness_score": 76,
    "overall_category": "HIGH"
  },
  "post_distribution": {
    "high_wellness_posts": 18,
    "moderate_wellness_posts": 5,
    "low_wellness_posts": 2
  },
  "content_analysis": {
    "most_common_positive_themes": [
      "gratitude",
      "personal_growth",
      "social_connection",
      "nature"
    ],
    "most_common_negative_themes": [
      "work_stress",
      "financial_worry"
    ],
    "activity_pattern": "active_contributor",
    "engagement_quality": "positive_and_supportive"
  },
  "insights": {
    "trend": "improving",
    "peak_wellness_period": "evenings",
    "main_wellness_drivers": [
      "outdoor_activities",
      "community_engagement",
      "creative_pursuits"
    ],
    "recommendations": [
      "Continue your outdoor activities",
      "Your community engagement is excellent",
      "Consider stress management techniques for work-related concerns"
    ]
  }
}
```

### Error Response Example

```json
{
  "success": false,
  "error": "MODEL_NOT_FOUND",
  "message": "The specified model file was not found: models/nonexistent_model.joblib",
  "details": {
    "requested_model": "models/nonexistent_model.joblib",
    "available_models": [
      "models/wellness_model_20251031_074843.joblib"
    ],
    "suggestion": "Please specify a valid model path or use the default model."
  },
  "timestamp": "2025-10-31T14:30:45Z"
}
```

---

## Model Training Output

### Complete Training Session Output

```
╔════════════════════════════════════════════════════════════╗
║         Mental Wellness Model Training Started             ║
╚════════════════════════════════════════════════════════════╝

📂 Loading Dataset...
   Path: Datasets/Social media & Mental Health/smmh.csv
   ✅ Dataset loaded successfully
   Shape: (1429, 17)

🔍 Data Overview:
   Total Records: 1,429
   Features: 17
   Target Variable: Depression_Level
   Missing Values: 0
   Duplicate Records: 0

📊 Class Distribution:
   Depression Level 1 (Minimal):     429 records (30.0%)
   Depression Level 2 (Mild):        358 records (25.1%)
   Depression Level 3 (Moderate):    392 records (27.4%)
   Depression Level 4 (Severe):      189 records (13.2%)
   Depression Level 5 (Very Severe): 61 records  (4.3%)

🔄 Preprocessing...
   ✅ Categorical features encoded
   ✅ Features normalized (MinMaxScaler)
   ✅ Data split completed

📈 Train/Val/Test Split:
   Training Set:   1,000 samples (70.0%)
   Validation Set:  215 samples  (15.0%)
   Test Set:        214 samples  (15.0%)

🤖 Training Random Forest Classifier...
   ⏳ Training in progress...
   
   Model Parameters:
   - n_estimators: 100
   - max_depth: 20
   - min_samples_split: 5
   - min_samples_leaf: 2
   - random_state: 42
   - n_jobs: -1

   ✅ Training completed in 15.3 seconds

📊 PERFORMANCE METRICS:

   ┌─────────────────────────────────────┐
   │ Overall Model Performance           │
   ├─────────────────────────────────────┤
   │ Accuracy:   87.50%                  │
   │ Precision:  85.20%                  │
   │ Recall:     89.10%                  │
   │ F1-Score:   87.10%                  │
   │ AUC Score:  0.9234                  │
   └─────────────────────────────────────┘

   Per-Class Performance:
   
   Class 1 (Minimal):
   ├─ Precision: 0.90
   ├─ Recall:    0.92
   ├─ F1-Score:  0.91
   └─ Support:   128
   
   Class 2 (Mild):
   ├─ Precision: 0.84
   ├─ Recall:    0.88
   ├─ F1-Score:  0.86
   └─ Support:   107
   
   Class 3 (Moderate):
   ├─ Precision: 0.86
   ├─ Recall:    0.85
   ├─ F1-Score:  0.86
   └─ Support:   118
   
   Class 4 (Severe):
   ├─ Precision: 0.79
   ├─ Recall:    0.82
   ├─ F1-Score:  0.80
   └─ Support:   52
   
   Class 5 (Very Severe):
   ├─ Precision: 0.75
   ├─ Recall:    0.71
   ├─ F1-Score:  0.73
   └─ Support:   14

📁 Saving Model...
   ✅ Model saved to: models/wellness_model_20251031_074843.joblib
   ✅ Metrics saved to: reports/wellness_model_20251031_074843_metrics.json
   ✅ Classification report saved

🎯 Feature Importance (Top 10):
   1. 🏆 Platform_Reddit:         0.187
   2. 🏆 Platform_Twitter:        0.164
   3. 🏆 Anxiety_Score:           0.145
   4. 🏆 Depression_Severity:     0.132
   5. 🏆 Sleep_Issues:            0.098
   6. 🏆 Social_Connection:       0.087
   7. 🏆 Treatment_History:       0.065
   8. 🏆 Substance_Use:           0.055
   9. 🏆 Media_Consumption:       0.051
   10. 🏆 Age_Group:              0.042

╔════════════════════════════════════════════════════════════╗
║            ✅ Training Complete!                           ║
╚════════════════════════════════════════════════════════════╝

📊 Model ready for inference. You can now:

   1. Make predictions on new data:
      python scripts/predict.py --model models/wellness_model_20251031_074843.joblib

   2. Evaluate on test set:
      python scripts/predict.py --model models/wellness_model_20251031_074843.joblib \
                                 --test_set data/test.csv

   3. Launch the web interface:
      python -m http.server 8000

```

---

## Batch Processing Example

### CSV Input File Format

**File: user_inputs.csv**
```csv
id,user_text
1,I'm feeling amazing and grateful today!
2,Struggling with anxiety and stress
3,Just had a nice day with friends
4,Everything feels overwhelming right now
5,Life is pretty good overall
```

### Processing Command

```bash
python scripts/predict.py --model models/wellness_model_20251031_074843.joblib \
  --input_file user_inputs.csv \
  --output_file predictions_output.csv
```

### Output CSV File

**File: predictions_output.csv**
```csv
id,user_text,depression_level,wellness_score,category,confidence
1,I'm feeling amazing and grateful today!,1,87,HIGH,0.92
2,Struggling with anxiety and stress,3,45,LOW,0.88
3,Just had a nice day with friends,2,71,MODERATE,0.85
4,Everything feels overwhelming right now,4,38,LOW,0.89
5,Life is pretty good overall,2,69,MODERATE,0.83
```

### Processing Output Log

```
📊 Batch Processing Started
─────────────────────────────────────

Input File: user_inputs.csv
Total Records: 5
Output File: predictions_output.csv

Processing: [████████████████████] 100% (5/5)

✅ Batch Processing Complete!

📈 Summary Statistics:
   Total Processed: 5
   Successful: 5
   Failed: 0
   
   Average Wellness Score: 62.0
   Average Confidence: 0.875
   
   Distribution:
   • High (≥75):      1 record
   • Moderate (50-74): 2 records
   • Low (<50):       2 records

💾 Results saved to: predictions_output.csv
```

---

## Evaluation Reports

### Sample Evaluation Report (JSON)

**File: reports/test_evaluation_report.md**

```json
{
  "evaluation_date": "2025-10-31",
  "model_name": "wellness_model_20251031_074843",
  "dataset": "test_dataset",
  "num_samples": 214,
  "num_classes": 5,
  "accuracy": 0.875,
  "precision": 0.852,
  "recall": 0.891,
  "f1_score": 0.871,
  "auc_score": 0.9234,
  "confusion_matrix": [
    [118, 8, 2, 0, 0],
    [5, 94, 8, 0, 0],
    [2, 10, 100, 6, 0],
    [0, 2, 5, 43, 2],
    [0, 0, 1, 3, 10]
  ],
  "class_distribution": {
    "1": 128,
    "2": 107,
    "3": 118,
    "4": 52,
    "5": 14
  },
  "precision_per_class": [0.90, 0.84, 0.86, 0.79, 0.75],
  "recall_per_class": [0.92, 0.88, 0.85, 0.82, 0.71],
  "f1_per_class": [0.91, 0.86, 0.86, 0.80, 0.73],
  "feature_importance": {
    "Platform_Reddit": 0.187,
    "Platform_Twitter": 0.164,
    "Anxiety_Score": 0.145,
    "Depression_Severity": 0.132,
    "Sleep_Issues": 0.098
  }
}
```

---

## Tips for Best Results

✅ **Input text should be:**
- At least 2-3 sentences for better analysis
- Representative of current emotional state
- Natural language (as you would normally write)

✅ **For batch processing:**
- Ensure CSV has an `id` and text column
- Text entries should not be empty
- Recommended: 10+ entries for meaningful statistics

✅ **For API usage:**
- Make requests with valid model paths
- Include proper error handling
- Cache results for frequently analyzed data

---

**Need more examples?** Check out the [main README](../README.md) or [SETUP.md](./SETUP.md).

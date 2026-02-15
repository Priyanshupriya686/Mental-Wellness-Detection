# ⚡ Quick Reference Guide

One-page quick reference for common commands and workflows.

---

## Installation (Copy & Paste)

### Windows
```powershell
git clone https://github.com/Priyanshupriya686/Mental-Wellness-Detection.git
cd Mental-Wellness-Detection
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### macOS/Linux
```bash
git clone https://github.com/Priyanshupriya686/Mental-Wellness-Detection.git
cd Mental-Wellness-Detection
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Common Commands

### 🔍 Single Prediction
```bash
python scripts/predict.py --model models/wellness_model_20251031_074843.joblib \
  --input "Your text here"
```

### 📊 Batch Processing
```bash
python scripts/predict.py --model models/wellness_model_20251031_074843.joblib \
  --input_file input.csv --output_file output.csv
```

### 🚂 Train New Model
```bash
python scripts/train.py --data Datasets/Social\ media\ \&\ Mental\ Health/smmh.csv
```

### 🌐 Launch Web App
```bash
python -m http.server 8000
```
Then open: `http://localhost:8000`

### 📉 Preprocess Data
```bash
python scripts/preprocess.py --input data.csv --output processed.csv
```

---

## Wellness Score Guide

| Score | Category | Emoji | Meaning |
|-------|----------|-------|---------|
| 75-100 | HIGH | 🟢 | Excellent well-being |
| 50-74 | MODERATE | 🟡 | Good overall wellness |
| 0-49 | LOW | 🔴 | May need support |

---

## Directory Structure

```
Mental-Wellness-Detection/
├── scripts/              # Python scripts
│   ├── train.py         # Training script
│   ├── predict.py       # Inference script
│   └── preprocess.py    # Data preprocessing
├── models/              # Saved models (.joblib)
├── Datasets/            # Training data
├── reports/             # Evaluation results
├── docs/                # Documentation
├── index.html           # Web interface
├── README.md            # Main documentation
├── SETUP.md             # Detailed setup guide
└── requirements.txt     # Python dependencies
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Module not found | `pip install -r requirements.txt` |
| Model not found | Check model path: `ls models/` |
| Permission denied | `chmod +x scripts/*.py` |
| API credentials error | Check `.env` file exists and has correct format |
| Port 8000 in use | Try: `python -m http.server 8001` |

---

## API Credentials Setup

Create `.env` file in project root:
```
REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USER_AGENT=MentalWellness/1.0
TWITTER_API_KEY=your_key
TWITTER_API_SECRET=your_secret
TWITTER_BEARER_TOKEN=your_token
```

---

## Key Resources

- 📖 **Detailed Setup**: [SETUP.md](./SETUP.md)
- 📸 **Examples**: [EXAMPLES.md](./EXAMPLES.md)
- 📚 **Main README**: [../README.md](../README.md)
- 🐛 **Issues**: [GitHub Issues](https://github.com/Priyanshupriya686/Mental-Wellness-Detection/issues)
- 🆘 **Crisis Support**: Call **988** (US) or text **HOME** to **741741**

---

## Model Information

- **Algorithm**: Random Forest Classifier
- **Training Data**: 1,429 social media mental health survey records
- **Accuracy**: 87.5%
- **Last Updated**: 2025-10-31
- **File**: `models/wellness_model_20251031_074843.joblib`

---

## Next Steps

1. **First Time?** → Go to [SETUP.md](./SETUP.md)
2. **Want Examples?** → Check [EXAMPLES.md](./EXAMPLES.md)
3. **Need Help?** → See Troubleshooting above
4. **Ready to Use?** → Run your first prediction!

---

**Happy analyzing! 🧠✨**

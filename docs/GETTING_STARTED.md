# 🎯 Getting Started - Visual Guide

A visual guide to help you navigate the documentation and get started quickly.

---

## Your Journey 🛤️

```
START HERE
    ↓
    ├─→ 📖 Read README.md Overview (2 min)
    │
    ├─→ 🚀 Quick Start Guide in README (5 min)
    │
    ├─→ Choose Your Path:
    │
    ├─ Path A: SETUP HELP? 
    │  └─→ 📋 SETUP.md (Windows/Mac/Linux) (15 min)
    │
    ├─ Path B: QUICK COMMANDS?
    │  └─→ ⚡ docs/QUICK_REFERENCE.md (2 min)
    │
    ├─ Path C: SEE EXAMPLES?
    │  └─→ 📸 docs/EXAMPLES.md (10 min)
    │
    └─ Path D: NEED JSON SAMPLES?
       └─→ 📁 docs/sample_outputs/ (reference)
    
    ↓
    ✅ Running predictions successfully!
```

---

## Documentation Map 🗺️

```
📦 Mental-Wellness-Detection/
│
├─ 📖 README.md
│  ├─ Overview & Features
│  ├─ 🚀 QUICK START GUIDE ← START HERE
│  ├─ Sample Outputs
│  └─ 📚 Documentation Links
│
├─ 📋 SETUP.md (NEW!)
│  ├─ Step-by-step setup for:
│  │  ├─ Windows
│  │  ├─ macOS
│  │  └─ Linux
│  ├─ API Credentials
│  └─ Troubleshooting
│
├─ 📁 docs/ (NEW!)
│  ├─ 📸 EXAMPLES.md (NEW!)
│  │  ├─ Web screenshots
│  │  ├─ CLI examples
│  │  ├─ JSON responses
│  │  └─ Training logs
│  │
│  ├─ ⚡ QUICK_REFERENCE.md (NEW!)
│  │  ├─ Copy-paste commands
│  │  ├─ Quick tables
│  │  └─ Troubleshooting
│  │
│  ├─ 📋 IMPROVEMENTS.md (NEW!)
│  │  └─ What was improved
│  │
│  └─ 📁 sample_outputs/ (NEW!)
│     ├─ positive_sentiment_example.json
│     ├─ negative_sentiment_example.json
│     ├─ batch_prediction_example.json
│     ├─ sample_input.csv
│     └─ sample_output.csv
│
└─ requirements.txt (NEW!)
   └─ All Python dependencies
```

---

## File Reference 📚

### Core Documentation

| File | Purpose | Read Time | Use When |
|------|---------|-----------|----------|
| **README.md** | Project overview + Quick Start | 10 min | Getting oriented |
| **SETUP.md** | Detailed setup instructions | 15 min | Setting up environment |
| **requirements.txt** | Python dependencies | - | Running `pip install` |

### Reference Documentation

| File | Purpose | Read Time | Use When |
|------|---------|-----------|----------|
| **docs/EXAMPLES.md** | Real examples & outputs | 10 min | Understanding outputs |
| **docs/QUICK_REFERENCE.md** | One-page commands | 2 min | Need quick commands |
| **docs/IMPROVEMENTS.md** | What was added | 5 min | Curious about changes |

### Sample Data

| File | Contents | Use Case |
|------|----------|----------|
| **sample_input.csv** | 10 text samples | Test batch processing |
| **sample_output.csv** | Prediction results | See expected output format |
| **positive_sentiment_example.json** | High wellness (87/100) | JSON response format |
| **negative_sentiment_example.json** | Low wellness (35/100) | Crisis recommendations |
| **batch_prediction_example.json** | 5-record batch | Batch JSON format |

---

## Quick Command Reference ⚡

### First-Time Setup

```bash
# 1. Clone & enter directory
git clone https://github.com/Priyanshupriya686/Mental-Wellness-Detection.git
cd Mental-Wellness-Detection

# 2. Create virtual environment
python -m venv venv

# 3. Activate (Windows: use .\venv\Scripts\Activate.ps1)
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# ✅ Done! Ready to use.
```

### Make Your First Prediction

```bash
python scripts/predict.py \
  --model models/wellness_model_20251031_074843.joblib \
  --input "I'm feeling great today!"
```

**Expected Output:**
```
🎯 Depression Level: 1
📊 Wellness Score: 85/100
✅ Category: HIGH
```

### Run Batch Predictions

```bash
python scripts/predict.py \
  --model models/wellness_model_20251031_074843.joblib \
  --input_file docs/sample_outputs/sample_input.csv \
  --output_file predictions.csv
```

### Launch Web App

```bash
python -m http.server 8000
# Then visit: http://localhost:8000
```

---

## Feature Highlights 🌟

### What You Get

✅ **Ready-to-use Model**
- Pre-trained Random Forest classifier
- 87.5% accuracy on test data
- Works out of the box

✅ **Multiple Input Methods**
- Single text analysis
- CSV batch processing
- Web interface
- API (JSON)

✅ **Comprehensive Outputs**
- Depression level (1-5)
- Wellness score (0-100)
- Confidence scores
- Detailed insights
- JSON responses

✅ **Crisis Support**
- 988 Suicide & Crisis Lifeline integration
- Crisis text line: TEXT HOME to 741741
- Emergency resource recommendations

---

## Typical Workflow 🔄

```
┌─────────────────────────────────────┐
│ 1. Setup (15 min, first time only) │
│    • Clone repo                      │
│    • Create venv                     │
│    • Install dependencies            │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 2. Prepare Input (1 min)             │
│    • Single text OR                  │
│    • CSV file with texts             │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 3. Run Prediction (10 sec)           │
│    python scripts/predict.py \       │
│      --model models/... \            │
│      --input "text..."               │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│ 4. Get Results (instant)             │
│    • Wellness score                  │
│    • Depression level                │
│    • Category & insights             │
│    • JSON response (if API mode)     │
└─────────────────────────────────────┘
```

---

## Common Workflows 🎯

### Analyze Your Own Text

```bash
# Simple command
python scripts/predict.py \
  --model models/wellness_model_20251031_074843.joblib \
  --input "Your feelings here..."

# See: docs/EXAMPLES.md for real examples
```

### Process Multiple Users' Posts

```bash
# Prepare CSV with user posts
# See: docs/sample_outputs/sample_input.csv

python scripts/predict.py \
  --model models/wellness_model_20251031_074843.joblib \
  --input_file users_data.csv \
  --output_file results.csv

# See: docs/sample_outputs/sample_output.csv for format
```

### Build on the Model

```bash
# Use existing model for your application
# See: docs/EXAMPLES.md for JSON response format

# Or retrain with your own data
python scripts/train.py --data your_data.csv
```

---

## Troubleshooting Quick Links 🔧

**Problem** → **Solution**

| Issue | Where to Find Help |
|-------|-------------------|
| "Module not found" | SETUP.md → Troubleshooting |
| Model file error | QUICK_REFERENCE.md → Common Commands |
| Can't activate venv | SETUP.md → (Your OS section) |
| API credentials? | SETUP.md → API Credentials Setup |
| What's the JSON format? | docs/EXAMPLES.md → Sample JSON |
| Want example commands? | docs/QUICK_REFERENCE.md |
| Confused about output? | docs/EXAMPLES.md → Command Line Examples |

---

## Glossary 📖

- **Wellness Score**: 0-100 scale, higher = better well-being
- **Depression Level**: 1-5 scale, higher = more depression indicators
- **Category**: HIGH (≥75), MODERATE (50-74), LOW (<50)
- **Confidence**: Model's certainty in the prediction (0-1)
- **Batch Processing**: Analyzing multiple texts in one run

---

## Next Steps 👉

1. **Read**: README.md (Quick Start section)
2. **Follow**: SETUP.md for your operating system
3. **Run**: Your first prediction command
4. **Explore**: Try the web interface at http://localhost:8000
5. **Experiment**: Use sample files in docs/sample_outputs/

---

## Support Resources 📞

| Topic | Resource |
|-------|----------|
| Setup Help | [SETUP.md](./SETUP.md) |
| Command Examples | [docs/EXAMPLES.md](./docs/EXAMPLES.md) |
| Quick Commands | [docs/QUICK_REFERENCE.md](./docs/QUICK_REFERENCE.md) |
| Sample Outputs | [docs/sample_outputs/](./docs/sample_outputs/) |
| Issues/Bugs | [GitHub Issues](https://github.com/Priyanshupriya686/Mental-Wellness-Detection/issues) |
| Crisis Support | **Call 988** (US) / **Text HOME to 741741** |

---

## You're All Set! 🎉

Everything you need is now documented and ready to use. 

**Estimated time to first prediction: 15 minutes**

Start with [README.md](./README.md) → Quick Start section!

---

*Last Updated: 2025-10-31*
*Status: ✅ Complete - Ready for users*

# 📋 Complete Setup Guide

This guide provides step-by-step instructions for setting up the Mental Wellness Detection system on different operating systems.

---

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Windows Setup](#windows-setup)
3. [macOS Setup](#macos-setup)
4. [Linux Setup](#linux-setup)
5. [API Credentials Setup](#api-credentials-setup)
6. [Troubleshooting](#troubleshooting)
7. [Verification](#verification)

---

## System Requirements

### Minimum Requirements
- **OS**: Windows 10+, macOS 10.14+, Ubuntu 18.04+
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Disk Space**: 2GB for dependencies and models
- **Internet**: Required for initial setup and API access

### Check Your Python Version
```bash
python --version
# Should output: Python 3.8.x or higher
```

If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/)

---

## Windows Setup

### Step 1: Clone the Repository

**Using Git:**
```powershell
git clone https://github.com/Priyanshupriya686/Mental-Wellness-Detection.git
cd Mental-Wellness-Detection
```

**Without Git (Download ZIP):**
1. Visit: https://github.com/Priyanshupriya686/Mental-Wellness-Detection
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file
4. Open PowerShell in the extracted folder

### Step 2: Create Virtual Environment

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1
```

**⚠️ If you get an execution policy error:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Then try activation again:
.\venv\Scripts\Activate.ps1
```

✅ You should see `(venv)` at the start of your command line.

### Step 3: Install Dependencies

```powershell
# Upgrade pip first
python -m pip install --upgrade pip

# Install all requirements
pip install -r requirements.txt
```

This will take 2-3 minutes. You should see:
```
Successfully installed pandas-1.3.5 scikit-learn-1.0.2 ...
```

### Step 4: Verify Installation

```powershell
python -c "import pandas; import sklearn; print('✅ All dependencies installed!')"
```

---

## macOS Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Priyanshupriya686/Mental-Wellness-Detection.git
cd Mental-Wellness-Detection
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

✅ You should see `(venv)` at the start of your command line.

### Step 3: Install Dependencies

```bash
# Upgrade pip first
python3 -m pip install --upgrade pip

# Install all requirements
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
python3 -c "import pandas; import sklearn; print('✅ All dependencies installed!')"
```

---

## Linux Setup (Ubuntu/Debian)

### Step 1: Install Python Development Headers

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv python3-dev
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/Priyanshupriya686/Mental-Wellness-Detection.git
cd Mental-Wellness-Detection
```

### Step 3: Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
# Upgrade pip
python3 -m pip install --upgrade pip

# Install all requirements
pip install -r requirements.txt
```

### Step 5: Verify Installation

```bash
python3 -c "import pandas; import sklearn; print('✅ All dependencies installed!')"
```

---

## API Credentials Setup

### Reddit API Credentials

1. **Create Reddit Account** (if you don't have one):
   - Go to https://www.reddit.com/register/
   - Complete registration

2. **Create Reddit Application**:
   - Go to https://www.reddit.com/prefs/apps
   - Click "Create Another App"
   - Fill in the form:
     - **Name**: "Mental Wellness Detection"
     - **Type**: Select "script"
     - **Redirect URI**: `http://localhost:8000` (or any valid URI)
   - Click "Create app"

3. **Get Your Credentials**:
   - **Client ID**: The random string under your app name
   - **Client Secret**: The long string labeled "secret"
   - **User Agent**: Create a unique identifier like `MentalWellness_v1.0`

4. **Create `.env` file** in the project root:
   ```
   REDDIT_CLIENT_ID=your_client_id_here
   REDDIT_CLIENT_SECRET=your_client_secret_here
   REDDIT_USER_AGENT=MentalWellness_v1.0
   ```

### Twitter API Credentials

1. **Apply for Developer Access**:
   - Go to https://developer.twitter.com/en/portal/dashboard
   - Click "Apply for access"
   - Select "Elevated" access
   - Complete the application form
   - Wait for approval (typically 5-10 minutes)

2. **Create a Project and App**:
   - Go to https://developer.twitter.com/en/portal/projects-and-apps
   - Click "Create Project"
   - Name it "Mental Wellness Detection"
   - Create an app within the project

3. **Get Your API Keys**:
   - Go to your app settings
   - Copy:
     - **API Key** (Consumer Key)
     - **API Secret** (Consumer Secret)
     - **Bearer Token**

4. **Add to `.env` file**:
   ```
   TWITTER_API_KEY=your_api_key_here
   TWITTER_API_SECRET=your_api_secret_here
   TWITTER_BEARER_TOKEN=your_bearer_token_here
   ```

5. **Protect Your Credentials**:
   ```bash
   # Never commit .env file to GitHub
   echo ".env" >> .gitignore
   ```

---

## First-Time Run

### Run a Quick Test

```bash
# Test 1: Load the existing model
python scripts/predict.py --model models/wellness_model_20251031_074843.joblib \
  --input "I'm feeling positive and grateful"
```

Expected output:
```
Input: I'm feeling positive and grateful
─────────────────────────────────────
✅ Model loaded successfully
🎯 Depression Level: 1
📊 Wellness Score: 85/100
✅ Category: HIGH
```

### Run Training (Optional - if you want to retrain the model)

```bash
python scripts/train.py --data Datasets/Social\ media\ \&\ Mental\ Health/smmh.csv \
  --model_dir models/ --test_size 0.15
```

This trains a new model and saves it to the `models/` directory.

### Launch Web Interface

```bash
# Start local server
python -m http.server 8000

# Then open your browser:
# http://localhost:8000
```

---

## Deactivate Virtual Environment

When you're done working, deactivate the virtual environment:

**Windows:**
```powershell
deactivate
```

**macOS/Linux:**
```bash
deactivate
```

---

## Troubleshooting

### Problem: "pip: command not found"
**Solution**: Use `python -m pip` instead:
```bash
python -m pip install -r requirements.txt
```

### Problem: "No module named 'sklearn'"
**Solution**: Reinstall scikit-learn:
```bash
pip install --force-reinstall scikit-learn
```

### Problem: Virtual environment activation fails
**Windows - ExecutionPolicy Error:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

**macOS/Linux - Permission Denied:**
```bash
chmod +x venv/bin/activate
source venv/bin/activate
```

### Problem: Model file not found
**Solution**: Ensure the model path is correct:
```bash
# List available models
dir models/  # Windows
ls models/   # macOS/Linux
```

### Problem: "No module named 'praw'" or "No module named 'tweepy'"
**Solution**: Install missing packages:
```bash
pip install praw tweepy
```

### Problem: Cannot connect to Reddit/Twitter API
**Possible causes:**
1. Invalid API credentials in `.env` file
2. API key rate limits exceeded (wait a few minutes)
3. Network connectivity issue
4. API service is down

**Solution**: 
- Verify credentials in `.env` file
- Check internet connection
- Test with a different network

---

## Verification

### Checklist: Environment Ready ✅

- [ ] Python 3.8+ installed: `python --version`
- [ ] Virtual environment created and activated
- [ ] All dependencies installed: `pip list`
- [ ] `.env` file created with API credentials
- [ ] Can load the model: `python scripts/predict.py`
- [ ] Can run predictions successfully
- [ ] Web interface loads: `http://localhost:8000`

### Test Commands

```bash
# Test 1: Import all required libraries
python -c "import pandas, numpy, sklearn, flask, praw, tweepy; print('✅ All imports successful!')"

# Test 2: Load the trained model
python scripts/predict.py --model models/wellness_model_20251031_074843.joblib \
  --input "test message"

# Test 3: List available models
python -c "from pathlib import Path; print([f.name for f in Path('models').glob('*.joblib')])"
```

All checks passing? 🎉 **You're ready to use the Mental Wellness Detection system!**

---

## Getting Help

If you encounter issues:

1. Check [Troubleshooting](#troubleshooting) section
2. Search existing GitHub issues: https://github.com/Priyanshupriya686/Mental-Wellness-Detection/issues
3. Create a new issue with:
   - Your operating system
   - Python version
   - Error message (full stack trace)
   - Steps to reproduce

---

**Happy analyzing! 🧠✨**

# 🏠 Virtual Environment (venv) - Complete User Guide

## 🔧 What is a Virtual Environment?

Think of it like having a **private workshop** in your garage:

- **Without venv**: Like working in a shared community workshop where everyone's tools get mixed up
- **With venv**: Like having your own private workshop with only YOUR tools and materials

## 🚪 How to Enter and Exit Your Workshop

### 📍 To ENTER your workshop (.venv):
```bash
# Navigate to your project folder first
cd /home/dci-student/Desktop/Workspace

# Activate your private workshop
source .venv/bin/activate
```

**You'll see this change in your terminal:**
```bash
# BEFORE (outside workshop):
dci-student@hostname:~/Desktop/Workspace$

# AFTER (inside workshop):
(.venv) dci-student@hostname:~/Desktop/Workspace$
```

### 🚪 To EXIT your workshop:
```bash
# Leave your private workshop
deactivate
```

## 💡 What Happens When You Turn Off Your Computer?

### 🔋 When Computer is OFF:
- ✅ **Your workshop STAYS BUILT** (the .venv folder remains)
- ✅ **All your tools are SAFE** (installed packages are saved)
- ❌ **But you're NOT inside it** (you need to "enter" again)

**Think of it like:** Your garage workshop stays built when you leave home, but you need to open the garage door and turn on the lights when you come back.

### 🖥️ When You Close VS Code:
- ✅ **Workshop stays built**
- ❌ **You're automatically "outside" the workshop**
- ❌ **Need to "enter" again next time**

## 📋 Step-by-Step Guidelines for Daily Use

### 🌅 Starting Your Work Day:

```bash
# DAILY STARTUP ROUTINE
# ====================

# 1. Open Terminal (Ctrl+Alt+T)
# 2. Navigate to your project
cd /home/dci-student/Desktop/Workspace

# 3. Enter your private workshop
source .venv/bin/activate

# 4. Verify you're inside (look for (.venv) in prompt)
# You should see: (.venv) dci-student@hostname:~/Desktop/Workspace$

# 5. Open VS Code from inside the environment
code .

# 6. Start working on your Bible analysis!
```

### 🌙 Ending Your Work Day:

```bash
# When you're done working:

# 1. Save all your work in VS Code
# 2. Close VS Code
# 3. In terminal, exit the workshop:
deactivate

# 4. You're now outside the workshop
# Terminal shows: dci-student@hostname:~/Desktop/Workspace$
```

## 🎯 Quick Commands Reference

```bash
# VIRTUAL ENVIRONMENT QUICK REFERENCE
# ===================================

# Check if you're inside the workshop:
echo $VIRTUAL_ENV
# Shows path if inside, empty if outside

# Enter workshop:
source .venv/bin/activate

# Exit workshop:
deactivate

# Check what tools you have installed:
pip list

# Install new tools (only when inside workshop):
pip install package-name

# Run your Bible analysis:
jupyter notebook
# or
python src/data/acquisition.py
```

## ⚠️ Important Rules

### ✅ DO THIS:
1. **Always activate venv BEFORE working** on your Bible project
2. **Install packages ONLY when inside venv**
3. **Check your terminal prompt** - look for `(.venv)`
4. **Navigate to project folder FIRST**, then activate

### ❌ DON'T DO THIS:
1. **Don't install packages when outside venv** (will mess up your system)
2. **Don't forget to activate** before running your code
3. **Don't delete the .venv folder** (you'll lose your workshop)

## 🔍 How to Check Everything is Working

Create a new Python file and run this to verify your setup:

```python
import sys
import os

print("🔍 ENVIRONMENT CHECK")
print("=" * 30)

# Check if in virtual environment
if 'VIRTUAL_ENV' in os.environ:
    print("✅ Inside virtual environment")
    print(f"📍 Environment path: {os.environ['VIRTUAL_ENV']}")
else:
    print("❌ NOT in virtual environment")
    print("💡 Run: source .venv/bin/activate")

# Check Python location
print(f"🐍 Python executable: {sys.executable}")

# Check if our packages are available
packages = ['pandas', 'numpy', 'matplotlib', 'nltk']
for package in packages:
    try:
        __import__(package)
        print(f"✅ {package} available")
    except ImportError:
        print(f"❌ {package} missing")
```

## 🎪 Real-World Example

**Tomorrow morning, you want to work on Bible analysis:**

1. **Open terminal** → `Ctrl+Alt+T`
2. **Go to project** → `cd /home/dci-student/Desktop/Workspace`
3. **Enter workshop** → `source .venv/bin/activate`
4. **See (.venv) in prompt** → You're ready!
5. **Open VS Code** → `code .`
6. **Work on your analysis** → Open notebooks, run code
7. **When done** → Close VS Code, type `deactivate`

## 🆘 If Something Goes Wrong

```bash
# If you can't activate:
ls -la .venv/  # Check if folder exists

# If .venv is missing, recreate it:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# If packages are missing:
source .venv/bin/activate
pip install -r requirements.txt

# If you see permission errors:
sudo chown -R $USER:$USER .venv/
```

## 🚀 Quick Test - Are You Ready?

Run these commands to test everything:

```bash
# 1. Go to project
cd /home/dci-student/Desktop/Workspace

# 2. Activate environment
source .venv/bin/activate

# 3. Check it worked (should see (.venv) in prompt)
echo "Current environment: $VIRTUAL_ENV"

# 4. Test Python packages
python -c "import pandas, numpy, matplotlib; print('✅ All packages working!')"

# 5. Test notebook
jupyter notebook --version

# If all above work, you're ready for Bible analysis! 🎉
```

## 🎓 Remember

The virtual environment is like a **private workshop** - you need to "open the door" (activate) every time you want to work, but once inside, you have all your specialized tools ready for Bible text analysis! 🛠️📚

---

**💡 Tip**: Bookmark this file! You'll refer to it often when starting your data science work.

**📅 Created**: October 2, 2025
**🎯 Purpose**: Bible Text Analysis Project
**👤 User**: dci-student

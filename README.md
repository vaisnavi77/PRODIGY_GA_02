# Task-02: Image Generation with Pre-trained Models
## Prodigy Infotech Internship

This project uses **Stable Diffusion 2.1** via the **Hugging Face Inference API**
to generate images from text prompts, served through a Flask web app.

---

## 🛠️ Setup & Run

### Step 1 — Get a Free Hugging Face Token
1. Go to https://huggingface.co/join and create a free account
2. Go to https://huggingface.co/settings/tokens
3. Click "New token" → name it anything → Role: Read → Copy the token

### Step 2 — Add your token to app.py
Open `app.py` and replace:
```
HF_TOKEN = os.getenv("HF_TOKEN", "YOUR_HUGGINGFACE_TOKEN_HERE")
```
with your actual token, OR set it as an environment variable:
```bash
# Windows (PowerShell)
$env:HF_TOKEN = "hf_xxxxxxxxxxxxxxxxxxxx"

# Mac/Linux
export HF_TOKEN="hf_xxxxxxxxxxxxxxxxxxxx"
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Run the app
```bash
python app.py
```

### Step 5 — Open in browser
Visit: http://127.0.0.1:5000

---

## 📁 Folder Structure
```
image_generation/
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Frontend UI
├── static/                 # (optional CSS/JS)
└── generated_images/       # Saved AI images
```

---

## ⚠️ Notes
- First request may be slow (model loading ~20s)
- Free Hugging Face tier has rate limits
- Images are saved automatically to `generated_images/`

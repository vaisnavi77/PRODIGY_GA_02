import os
import io
import base64
import requests
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

HF_TOKEN = "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"

SAVE_DIR = os.path.join(os.path.dirname(__file__), "generated_images")
os.makedirs(SAVE_DIR, exist_ok=True)


def generate_image(prompt: str) -> dict:
    try:
        from huggingface_hub import InferenceClient
        client = InferenceClient(
            provider="fal-ai",
            api_key=HF_TOKEN,
        )
        image = client.text_to_image(
            prompt=prompt,
            model="black-forest-labs/FLUX.1-schnell",
        )
        # Save image
        filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(SAVE_DIR, filename)
        image.save(filepath)

        # Convert to base64
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")

        return {"success": True, "image": encoded, "filename": filename}

    except Exception as e:
        return {"success": False, "error": str(e)}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "").strip()
    if not prompt:
        return jsonify({"success": False, "error": "Please enter a prompt."})
    result = generate_image(prompt)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
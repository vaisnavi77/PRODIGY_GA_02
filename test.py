import requests

TOKEN = "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"

r = requests.post(
    "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1",
    headers={"Authorization": f"Bearer {TOKEN}"},
    json={"inputs": "a red apple"},
    timeout=30
)

print("Status:", r.status_code)
print("Response:", r.text[:300])
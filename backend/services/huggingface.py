import requests
from config import Config

def generate_questionnaire(scraped_data):
    print("generate_questionnaire called with scraped_data:", scraped_data)
    headers = {
        "Authorization": f"Bearer {Config.HUGGINGFACE_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"inputs": scraped_data["content"]}
    print("Sending request to Hugging Face API...")
    response = requests.post(
        "https://api-inference.huggingface.co/models/gpt2",
        headers=headers, json=payload
    )
    if response.status_code != 200:
        raise Exception("Failed to process with Hugging Face API")
    print("Sending request to Hugging Face API...")
    return response.json()

import requests
import json

URL = "https://api.openai.com/v1/images/generations"

def gen(prompt, model, VOTRE_API):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {VOTRE_API}"
    }

    data = {
        "model": model,
        "prompt": prompt,
        "num_images": 1,
        "size": "1024x1024",
        "response_format": "url"
    }

    resp = requests.post(URL, headers=headers, data=json.dumps(data))

    if resp.status_code != 200:
        raise ValueError("Erreur : " + resp.text)

    reponse = json.loads(resp.text)
    return reponse['data'][0]['url']

def telechargemont(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)

VOTRE_API = "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"
model = "image-alpha-001"

prompt = input("Mot clé de l'image :")

image_url = gen(prompt, model, VOTRE_API)

filename = prompt.replace(" ", "_") + ".jpg"
telechargemont(image_url, filename)

print(f"{filename} téléchargé avec succès")
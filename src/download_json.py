import requests

def download_json(url, save_path):
    response = requests.get(url)
    response.raise_for_status()  # Проверка успешности загрузки

    with open(save_path, 'wb') as file:
        file.write(response.content)

    print(f"JSON data downloaded and saved to {save_path}")

if __name__ == "__main__":
    url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
    save_path = "../deviation.json"
    download_json(url, save_path)

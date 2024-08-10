import json
import os
import requests
import tqdm

pdf_files_json = "./pdf_files.json"
pdf_dir = './pdfs'

if not os.path.exists(pdf_dir):
    os.makedirs(pdf_dir)

with open(pdf_files_json, "r") as file:
    pdf_files = json.load(file)


def download_pdf(url, file_name):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()

        with open(file_name, "wb") as file:
            file.write(response.content)
    except requests.exceptions.RequestException as e:
        print(f"Failed to download PDF. Error: {str(e)}")


def get_file_name(url):
    return url.split("/")[-1]


for pdf_file in tqdm.tqdm(pdf_files):
    file_name = get_file_name(pdf_file["url"])
    if not file_name or not file_name.lower().endswith(".pdf"):
        continue

    file_name = os.path.join(pdf_dir, file_name)

    if os.path.exists(file_name):
        pdf_file['downloaded'] = True
        pdf_file['downloaded_file'] = file_name
        print(f"PDF already exists at {file_name}")
        continue

    download_pdf(pdf_file["url"], file_name)

    pdf_file['downloaded'] = True
    pdf_file['downloaded_file'] = file_name
    print(f"Downloaded {file_name}")

with open(pdf_files_json, "w") as file:
    json.dump(pdf_files, file, indent=2, sort_keys=True, ensure_ascii=False)

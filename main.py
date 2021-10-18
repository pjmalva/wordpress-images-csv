import csv
from os import path
import urllib.request
from pathlib import Path

remove_str = "https://www.donadecasamoderninha.com.br/"

products = []
images = []

def download_image(url, image):
    return urllib.request.urlretrieve(url, image)

def create_path(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)

def prepare_path_image_name(url: str):
    url_striped = url.replace(remove_str, '')
    url_array = url_striped.split('/')
    return "/".join(url_array[:-1]).strip(), url_array[-1]

def download_image_from_url(url: str):
    folder, image = prepare_path_image_name(url)
    full_path = folder + "/" + image

    if path.exists(full_path):
        print('Já existe')
        return

    create_path(folder)
    return download_image(url, full_path)

with open('products.csv', 'r', encoding='utf8') as file:
    csv_file = csv.reader(file)

    for line in csv_file:
        products.append(line)

for product in products[1:]:
    rawImages = product[29]
    arrImages = rawImages.split(',')
    images += arrImages

images = set(images)

for index, image in enumerate(images):
    print("Downloading", index + 1, len(images), image)
    download = download_image_from_url(image)

print("Finished")

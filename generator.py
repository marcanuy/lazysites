import os
from bs4 import BeautifulSoup

LAZYIMAGE_CLASS = "lazyimage"

def fix_images_in_html(file_path):
    
    with open(file_path, "r") as f:
        contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')

    for img_tag in soup.find_all("img"):
        print("Before: {0}".format(img_tag))

        if LAZYIMAGE_CLASS not in img_tag:
            current_classes = img_tag.get('class', [])
            img_tag['class'] =  current_classes + [LAZYIMAGE_CLASS]
        print("After: {0} \n".format(img_tag))

    with open(file_path, "w") as f:
        f.write(str(soup))

for root, dirs, files in os.walk("public"):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            fix_images_in_html(file_path)

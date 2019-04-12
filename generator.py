import os
from bs4 import BeautifulSoup

LAZYIMAGE_CLASS = "lazyimage"

def fix_images_in_html(file_path):
    
    with open(file_path, "r") as f:
        contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')

    for img_tag in soup.find_all("img"):
        print("\nProcessing: {0}".format(img_tag))

        # add class
        current_classes = img_tag.get('class', [])
        if LAZYIMAGE_CLASS not in current_classes:
            img_tag['class'] =  current_classes + [LAZYIMAGE_CLASS]
        # add data-src
        if 'src' in img_tag.attrs: #3 and 'data-src' not in img_tag:
            img_tag['data-src'] = img_tag['src']
        print("After: {0} \n".format(img_tag))

    with open(file_path, "w") as f:
        f.write(str(soup))

for root, dirs, files in os.walk("public"):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            fix_images_in_html(file_path)

import os
from bs4 import BeautifulSoup

LAZYIMAGE_CLASS = "lazyimage"
LAZYIMAGE_JS_LIB_HTML = '<script src="https://cdn.jsdelivr.net/npm/lazysizes@4.1.7/lazysizes.js"></script>'


def fix_images_in_html(file_path):
    """Modify an html file"""
    
    with open(file_path, "r") as f:
        contents = f.read()
    print("\nProcessing: {0}".format(file_path))
    soup = BeautifulSoup(contents, 'html.parser')

    for img_tag in soup.find_all("img"):
        # add class
        current_classes = img_tag.get('class', [])
        if LAZYIMAGE_CLASS not in current_classes:
            img_tag['class'] =  current_classes + [LAZYIMAGE_CLASS]
        # add data-src
        if 'src' in img_tag.attrs: #3 and 'data-src' not in img_tag:
            img_tag['data-src'] = img_tag['src']

    # add js library if not present and some tag is using it
    lazyimage_soup = BeautifulSoup(LAZYIMAGE_JS_LIB_HTML, 'html.parser')
    body = soup.body
    if body and LAZYIMAGE_CLASS in str(body) and 'lazysizes.js' not in str(body):
        body.append(lazyimage_soup.script)

    with open(file_path, "w") as f:
        f.write(str(soup))

for root, dirs, files in os.walk("public"):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            fix_images_in_html(file_path)

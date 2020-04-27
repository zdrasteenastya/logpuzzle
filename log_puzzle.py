"""Collect puzzle"""

import os
import re
import requests


def read_urls(filename):
    """Collect needed urls from the input file"""

    # Retrieve the service name
    name_server = re.search(r'_\S+', filename).group()[1:-4]
    # Open file with img urls
    list_url = []
    with open(filename, 'r') as my_file:
        # Search Urls
        for line in my_file:
            uri = re.search(r'GET /\S+', line)
            if uri:
                get_url = uri.group()[4:]
                url_jpg = re.search(r'\S+.jpg', get_url)
                # Search only .jpg
                if url_jpg:
                    list_url.append('http://{0}{1}'.format(name_server, url_jpg))

    # Remove duplicates
    return sorted(set(list_url))


def download_images(list_url, dest_dir):
    """Request parts of puzzle"""

    # Create new dir if needed
    try:
        os.mkdir(dest_dir)
    except FileExistsError:
        print('This dir was already created')

    # List for save all image's names
    list_names = []
    os.chdir(dest_dir)
    # Find and download img
    for index, url in enumerate(list_url):
        img_name = 'img{0}.jpg'.format(index)
        with open(img_name, 'wb') as out_file:
            out_file.write(requests.get(url).content)
        list_names.append(img_name)
        print('Download!')

    # Create html
    with open('index1.html', 'w') as file_html:
        for tag in ('<verbatim>', '<html>', '<body>'):
            file_html.write(tag + '\n')
        cur_dict = os.getcwd()
        for pic_name in list_names:
            file_html.write('<img src ={}{}{}{}{}{}'.format(
                '"', cur_dict, '\\', pic_name, '"', '>'))
        file_html.write('\n{}{}{}'.format('</body>', '\n', '</html>'))
        file_html.close()
    return


def main():
    """The main fuction"""
    list_url = read_urls(r'animal_code.google.com.txt')
    download_images(list_url, 'animal')


if __name__ == "__main__":
    main()

import re
import os
import requests

def read_urls(filename):
    # Retrieve the service name
    name_server = re.search(r'_\S+',filename)
    name_server = name_server.group()
    name_server = name_server[:-4]
    name_server = name_server[1:]
    # Open file with img urls
    my_file = open(filename, 'r')
    list_url = []
    # Search Urls
    for l in my_file:
        r = re.search(r'GET /\S+', l)
        if r:
            get_url = r.group()
            my_url = get_url[4:]
            url_jpg = re.search(r'\S+.jpg',my_url)
    # Search only .jpg
            if url_jpg:                
                list_url.append('http://'+name_server+url_jpg.group())        

    # Remove duplicates
    list_url_uniq = set(list_url)
    list_url_uniq = sorted(list_url_uniq)
    #for st in list_url_uniq:
    #    print (st)
    return list_url_uniq

def download_images(list_url,dest_dir):
    # Create new dir if needed
    try:
        os.mkdir(dest_dir)
    except FileExistsError:
        print('This dir was already created')
    # Counter for numbering images
    i=0
    # List for save all image's names
    list_names = []
    os.chdir(dest_dir)
    # Find and download img
    for l in list_url:
        name_gen = 'img{0}.jpg'
        img_name = name_gen.format(i)
        img = requests.get(l)
        out = open(img_name, "wb")
        out.write(img.content)
        list_names.append(img_name)
        out.close()
        print ('Download!')
        i = i+1
    # Create html
    file_html = open('index1.html', "w")
    text = ['<verbatim>','<html>','<body>']
    for t in text:
        file_html.write(t+'\n')
    file_html.close()
    file_html = open('index1.html', "a")
    all_img = os.listdir()
    cur_dict = os.getcwd()
    for pic_name in list_names:
        a = '<img src ='+'"'+cur_dict+'\\'+pic_name+'"'+'>'
        file_html.write(a)
    file_html.write('\n'+'</body>'+'\n'+'</html>')
    file_html.close()
    return
    

def main():
    list_url = read_urls(r'animal_code.google.com.txt')
    download_images(list_url, 'animal') 
main()

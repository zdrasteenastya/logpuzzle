import re
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
def read_urls(filename):
    name_server = re.search(r'_\S+',filename)
    name_server = name_server.group()
    name_server = name_server[:-4]
    name_server = name_server[1:]
    my_file = open(filename, 'r')
    list_url = []
    for l in my_file:
        r = re.search(r'GET /\S+', l)
        if r:
            get_url = r.group()
            my_url = get_url[4:]
            url_jpg = re.search(r'\S+.jpg',my_url)
            if url_jpg:                
                list_url.append('http://'+name_server+url_jpg.group())        
    print (len(list_url))
    list_url_uniq = set(list_url)
    list_url_uniq = sorted(list_url_uniq)
    for st in list_url_uniq:
        print (st)
    return

def main():
    a = read_urls(r'animal_code.google.com.txt')    
main()

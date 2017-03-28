import requests
    
def pars(count):
  r = requests.get(count)
  text = r.text
  from bs4 import BeautifulSoup as bs
  soup = bs(text, "html.parser")
  h3 = soup("h3")
  res = {}
  for elem in h3:
      a_tag_list = elem.find_all("a")
      for a_tag in a_tag_list:
        res[a_tag.text] = a_tag.get("href")
  for key, value in res.items():
      res1 = value.replace("/url?q=","")
      res[key] = res1.split("&")[0]
  return res

def main():
    res = pars("https://www.google.ru/search?q=%D1%8E%D0%BC%D0%B8%D1%82%D0%B5%D1%80&oq=%D1%8E%D0%BC%D0%B8%D1%82%D0%B5%D1%80&aqs=chrome..69i57j0l2.2353j0j9&sourceid=chrome&ie=UTF-8#newwindow=1&q=%D1%8E%D0%BF%D0%B8%D1%82%D0%B5%D1%80&*")
    print (res)
main()

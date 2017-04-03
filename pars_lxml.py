import requests 
from lxml import html 
from lxml import etree 


def pars(count): 
    r = requests.get(count) 
    text = html.fromstring(r.text) 
    h3 = text.xpath('//h3//a') 
    res = {} 
    for elem in h3: 
        res[elem.text] = elem.get("href").replace("/url?q=", "").split("&")[0] 
    return res 


def main(): 
    res = pars("https://www.google.ru/search?q=%D1%8E%D0%BF%D0%B8%D1%82%D0%B5%D1%80&oq=%D1%8E%D0%BF%D0%B8%D1%82%D0%B5%D1%80&aqs=chrome..69i57j0l5.1274j0j9&sourceid=chrome&ie=UTF-8")
    names = res.keys() 
    for n in names: 
        print (n, res[n])


main()

from pip._vendor import requests

def htmlkoda():
    site = requests.get("https://www.rtvslo.si/iskalnik?q=iskalni niz")
    return site.text



#kds = htmlkoda()
#print(kds)
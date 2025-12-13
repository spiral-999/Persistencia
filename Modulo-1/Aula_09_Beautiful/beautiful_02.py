import requests
from bs4 import BeautifulSoup

with open("../Persistencia/Aula_09_Beautiful/beautiful_02.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

#print(soup.prettify()) # formata tudo
#print(soup.title.name) # nome da tag
print(soup.title.get_text())
print(soup.title.string) # funciona igual o get_text()

print(soup.p) # pega o primeiro paragrafo
print(soup.p["class"])

for link in soup.find_all("a"): # pega todos os links
    print(link)
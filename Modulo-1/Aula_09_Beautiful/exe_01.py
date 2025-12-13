# imprimir:
# o texto do <title>
# o conteúdo da <meta name="description" />, ou seja, o "content"
from bs4 import BeautifulSoup

with open("../Persistencia/Aula_09_Beautiful/exe_01.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

print(soup.title.string)
print(soup.title.get_text())
print(soup.find("title").string)
print(soup.find("title").get_text())

tag_meta_description = soup.find("meta", {"name":"description"})
print(tag_meta_description["content"])
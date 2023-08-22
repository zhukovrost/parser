import requests
from bs4 import BeautifulSoup
from json import dumps

url = "https://www.perfect-english-grammar.com/grammar-exercises.html"
html_content = requests.get(url).text

themes_array = []
for theme in BeautifulSoup(html_content, "lxml").find("section").find_all("b"):
    themes_array.append(theme.text.replace(':', ''))

f = open('themes.json', 'r+')
f.write(dumps(themes_array))
f.close()
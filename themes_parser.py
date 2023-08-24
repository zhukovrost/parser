import requests
from bs4 import BeautifulSoup
from json import dumps
from colorama import Fore

url = "https://www.perfect-english-grammar.com/grammar-exercises.html"
html_content = requests.get(url).text

themes_array = []

print(Fore.GREEN)
for theme in BeautifulSoup(html_content, "lxml").find("section").find_all("b"):
    formatted_theme = theme.text.replace(':', '')
    print(formatted_theme)
    themes_array.append(formatted_theme)

with open("themes.json", "r+") as f:
    f.write(dumps(themes_array))

print(Fore.MAGENTA + f"Total themes: {len(themes_array)}")

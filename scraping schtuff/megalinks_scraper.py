import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore
import os

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ*"
for i in alphabet:
    with open ("mega_scraped_links" + i + ".txt", "r") as f:
        with open ("mega_scraped_material" + i + ".txt", "x") as f2:
            for line in f:
                r = requests.get(line.strip())
                soup = BeautifulSoup(r.content, "html.parser")
                s = soup.find_all('div', class_="p-5 md:p-8")
                content = soup.find_all('div', class_="break-words meaning mb-4")
                content2 = soup.find_all('div', class_="break-words example italic mb-4")
                for j in content:
                    f2.write(j.text + "\n")
                for j in content2:
                    f2.write(j.text + "\n")
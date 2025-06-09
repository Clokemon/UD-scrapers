import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore
import os
import random

alphabetAgain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ*"
alphabet = list(alphabetAgain)

t = 1

for i in alphabet:
    if os.path.exists("mini_scraped_links" + i + ".txt"):
        alphabet.pop(alphabetAgain.find(i))
        alphabetAgain = "".join(alphabet)
        print("File mini_scraped_links" + i + ".txt already exists, skipping...")

for i in alphabet:
    f = open("mini_scraped_links" + i +".txt", "x")
    with open("mini_scraped_links" + i +".txt", "a") as f:
        t = 0
        while True:
            t += 1
            r = requests.get("https://www.urbandictionary.com/browse.php?character=" + i +"&page=" + str(t))
            soup = BeautifulSoup(r.content, "html.parser")
            s = soup.find("ul", class_="mt-3 columns-2 md:columns-3")
            content = soup.find_all('a', class_="py-1 block text-denim dark:text-white break-all hover:text-limon-lime hover:underline")
            if not content:
                break
            for j in content:
                f.write("https://www.urbandictionary.com" + j['href'] + "&page=" + str(1) + "\n")
                print("https://www.urbandictionary.com" + j['href'] + "&page=" + str(1) + "\n")
                
print("Done scraping mini links!")

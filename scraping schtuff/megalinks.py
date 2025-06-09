import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore
import os

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXY*"
alphabetToPageNo = {}

i = input("Enter the letter you want to scrape (A-Z): ").upper()

if not os.path.exists("mega_scraped_links.txt"):
    f = open("mega_scraped_links" + i +".txt", "w")
else:
    f = open("mega_scraped_links" + i +".txt", "w")
# counter fnaggling
t = 1
x = 1

for _ in range(1):
    with open("mega_scraped_links" + i + ".txt", "a") as f:
        t = 0
        f.write("https://www.urbandictionary.com/browse.php?character=" + i + "\n")
        while True:
            t += 1
            r = requests.get("https://www.urbandictionary.com/browse.php?character=" + i +"&page=" + str(t))
            soup = BeautifulSoup(r.content, "html.parser")
            s = soup.find("ul", class_="mt-3 columns-2 md:columns-3")
            content = soup.find_all('a', class_="py-1 block text-denim dark:text-white break-all hover:text-limon-lime hover:underline")
            if not content:
                break
            for j in content:
                x = 0
                while True:
                    x += 1
                    rx = requests.get("https://www.urbandictionary.com" + j['href'] + "&page=" + str(x))
                    soupx = BeautifulSoup(rx.content, "html.parser")
                    contentx = soupx.find('ul', class_="mt-5 list-none")
                    contentTest = soupx.find('body', class_="bg-ud-black font-sans min-h-screen flex items-center justify-center")
                    if contentx or contentTest:
                        break
                    else:
                        f.write("https://www.urbandictionary.com" + j['href'] + "&page=" + str(x) + "\n")
                        print("https://www.urbandictionary.com" + j['href'] + "&page=" + str(x) + "\n")
print("done")

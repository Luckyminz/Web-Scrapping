import requests
from bs4 import BeautifulSoup

html_text=requests.get("https://www.bbc.com/").text

soup=BeautifulSoup(html_text,"lxml")

right_side_bar=soup.find("div",class_="sc-666b6d83-0 sc-d72eeb81-3 jQlQXm cTzpUB")

for news in right_side_bar:
    new=news.find("h2", class_="sc-fa814188-3 iCfgww").get_text(strip=True)
    time=news.find("span",class_="sc-1907e52a-1 bZuSaP").get_text(strip=True)
    location=news.find("span", class_="sc-1907e52a-2 dIrLFx").get_text(strip=True)
    print(f"News : {new}")
    print(f"{time} | {location}")

    print()

# top_left_bar=soup.find_all("div",class_="sc-666b6d83-0 sc-d72eeb81-1 iiYaEO kTovqr")
#
# for topnews in top_left_bar:
#     topnew=topnews.find("div" ,class_="sc-fa814188-1 iRoJZi").find("h2",class_="sc-fa814188-3 iCfgww").get_text(strip=True)
#     print(topnew)
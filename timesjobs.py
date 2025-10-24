import requests
from bs4 import BeautifulSoup

html_text =requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=cybersecurity&txtLocation=").text

soup =BeautifulSoup(html_text,"lxml")

Jobs=soup.find_all("li",class_="clearfix job-bx wht-shd-bx")

print("Lastest job post in Cybersecurity.....")

print("Loading .....")
print()

for job in Jobs:
  postname=job.find("h2",class_="heading-trun").get_text(strip=True)
  location=job.find("div" ,class_="d-flex d-flex-l-r d-flex-align-item").find("li", class_="srp-zindex location-tru").get_text(strip=True)
  experience=job.find("div" ,class_="d-flex d-flex-l-r d-flex-align-item").find_all("li")[1].get_text(strip=True)
  company_name=job.find("header",class_="clearfix").find("h3",class_="joblist-comp-name").get_text(strip=True)
  Posted_date=job.find("header",class_="clearfix").find("span",class_="sim-posted").find("span").get_text(strip=True)
  print(f"Company Name : {company_name}")
  print(f"Post : {postname}")
  print(f"Location : {location}")
  print(f"Experience : {experience}")
  print(f"Job-posted-Date : {Posted_date}")

  print()

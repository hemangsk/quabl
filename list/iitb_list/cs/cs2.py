from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
url="https://www.cse.iitb.ac.in/page222?batch=MTech3"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
cl=browser.find_elements_by_xpath("//tr/td/a/b")
for c in cl:
	profile={}
	profile["name"]=c.text.strip()
	profile["name"]
	data.append(profile)
s="row2"

with open("16.json","w") as f:
	json.dump(data,f)	


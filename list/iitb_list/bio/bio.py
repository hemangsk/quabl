from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
url="http://www.bio.iitb.ac.in/people/students/dual-degree"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
cl=browser.find_elements_by_xpath("//table/tbody/tr/td")
i=0
for c in cl:
	i+=1
	if(i%4!=2):
		continue
	profile={}
	profile["name"]=c.text.strip()
	data.append(profile)
with open("dd.json","w") as f:
	json.dump(data,f)	


from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
import time
url="http://www.cse.iitk.ac.in/pages/MTech2013_Person.html"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
cl=browser.find_elements_by_xpath("//tbody/tr/td")
for c in cl:
	profile={}
	temp=c.text.strip()
	if temp[0] in '123456789':
		continue
	profile["name"]=temp
	data.append(profile)
with open("m13.json","w") as f:
	json.dump(data,f)	


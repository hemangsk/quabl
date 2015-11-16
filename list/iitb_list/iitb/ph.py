from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
import time
url="http://www.phy.iitb.ac.in/en/phd-student"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
cl=browser.find_elements_by_xpath("//tr/td/div/span")
i=0
for c in cl:
	i+=1
	if(i%3!=1):
		continue
	profile={}
	temp=c.text.strip()
	profile["name"]=temp
	data.append(profile)
with open("phd.json","w") as f:
	json.dump(data,f)	


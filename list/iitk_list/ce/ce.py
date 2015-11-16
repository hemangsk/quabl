from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
import time
url="http://www.iitk.ac.in/civil/ph-d-students"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
#cl=browser.find_elements_by_xpath("//tbody/tr/td/p")
cl=browser.find_elements_by_xpath("//h3")
i=0
for c in cl:
	profile={}
	temp=c.text.strip()
	if temp[0] in '123456789qwertyuiopasdfghjklzxcvbnm':
		continue
	profile["name"]=temp
	data.append(profile)
with open("ce_phd.json","w") as f:
	json.dump(data,f)	


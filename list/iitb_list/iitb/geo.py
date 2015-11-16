from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
url="http://www.geos.iitb.ac.in/index.php/en/people/278"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
cl=browser.find_elements_by_xpath("//ul/li")
i=0
for c in cl:
	i+=1
	profile={}
	temp=c.text.strip()
	profile["name"]=''
	for t in temp :
		if t in "01\n":
			break
		profile["name"]+=t
	data.append(profile)
with open("msc_geop.json","w") as f:
	json.dump(data,f)	


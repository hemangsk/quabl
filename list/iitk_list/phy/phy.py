from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
import time
url="http://www.iitk.ac.in/phy/index.php/people/phd-students"
browser=webdriver.Chrome()
browser.get(url)
data=[]

#cl=browser.find_elements_by_xpath("//h3")
i=0
soup=bs(browser.page_source)
cl=browser.find_elements_by_xpath("//tbody/tr/td")
for c in cl:
	i+=1
	if(i%5!=3):
		continue
	profile={}
	temp=c.text.strip()
	if temp=='':
		continue
	if temp[0] in '123456789qwertyuiopasdfghjklzxcvbnm':
		continue
			
	profile["name"]=temp
	data.append(profile)
with open("phy_phd.json","w") as f:
	json.dump(data,f)	


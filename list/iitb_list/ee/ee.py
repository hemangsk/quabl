from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import json
url="https://www.ee.iitb.ac.in/web/people/student_list/mtech/es"
browser=webdriver.Chrome()
browser.get(url)
soup=bs(browser.page_source)
data=[]
cl=browser.find_elements_by_xpath("//tr/td[@valign='top']")
i=0
for c in cl:
	i+=1
	if(i%3!=0):
		continue
	profile={}
	profile["name"]=c.text.strip()
	data.append(profile)
with open("mtech_es.json","w") as f:
	json.dump(data,f)	


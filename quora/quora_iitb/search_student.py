import quora_scrape
from selenium import webdriver
import json
import time
i=1485
j=0
def search(name,browser):
	global j
	global i
	j+=1
	if j<377+13+498+763+289+1323:
		return []
	profiles_list=[]
	iit=' Indian Institute of Technology, Bombay'
	link="https://www.quora.com/search?q="+name+iit+"&type=profile"
	time.sleep(1)
	for profile in quora_scrape.get_quora_data(link,browser):
		i=i+1
		stdinfo=str(i)+'.json'
		with open(stdinfo,'w') as f:
			f.write(profile)
		
	return profiles_list

def run_all(studentlist):
    browser=webdriver.Chrome()
    login = raw_input('Logged in to Quora? ')
    if login=='y':
        for student in studentlist:
            profiles=search(student['name'],browser)
            student['profiles']=profiles
            print 'got data for '+student['name']
        return studentlist

'''def test():
    std_data=[];
    with open('stdlist.json') as stdjson:
        std_data=json.load(stdjson)
    subdata=std_data[143:153]
    print run_all(subdata)'''

def contains(string,sub):
    return string.find(sub)>=0
	
def scrape_all():
    std_data=[];
    with open('iitb.json') as stdjson:
        std_data=json.load(stdjson)
    data_all= run_all(std_data)
scrape_all()

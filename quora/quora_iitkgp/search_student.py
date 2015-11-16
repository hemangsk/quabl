import quora_scrape
from selenium import webdriver
import json
import time
i=4128
j=0
def search(name,browser):
	global i
    #nm=''
    #for n in name:
    #    if n==' ':
    #        nm+='%'
    #    else:
    #        nm+=n
	profiles_list=[]
	iit=' Indian Institute of Technology, Kharagpur'
	link="https://www.quora.com/search?q="+name+iit+"&type=profile"
	time.sleep(1)
	for profile in quora_scrape.get_quora_data(link,browser):
		'''print profile
		profiles={}
		data=[]
		profiles['quora']=profile
		if('about' in profile):
			name=profile['about']
			if(contains(name,'IITM') or contains(name,'Madras')):'''
		i=i+1
		stdinfo=str(i)+'.json'
		with open(stdinfo,'w') as f:
			#json.dump(profile,f)
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

def test():
    std_data=[];
    with open('stdlist.json') as stdjson:
        std_data=json.load(stdjson)
    subdata=std_data[143:153]
    print run_all(subdata)

def contains(string,sub):
    return string.find(sub)>=0
	
def scrape_all():
    std_data=[];
    with open('stdinfo.json','w') as f:
        json.dump([],f)
    with open('iitkgp1.json') as stdjson:
        std_data=json.load(stdjson)
    data_all= run_all(std_data)
scrape_all()

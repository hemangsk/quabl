from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from selenium import webdriver
import quora
import time

def y(a=[0]):
    a[0] += 1
    print "total"
    print a  
def parse_page(browser,soup):
	list_u = []
	p=soup.find(class_='grid_page_center_col results_list')
	profiles=soup.find_all(class_='pagedlist_item')
	for profile in profiles:
	    time.sleep(1)
	    l=profile.find('a')
	    link=l['href']
	    if link.startswith('http'):
	    	continue
	    u='https://www.quora.com'+link
	    data=quora.get_quora_data(u,browser)
	    if(data):
	    	list_u.append(data)
	return list_u
def parse(browser,url):
	html=browser.page_source
	soup=bs(html)
	data={}
	return parse_page(browser,soup)


import requests 

def get_data(browser):
    browser.get(url)
    return parse(browser,browser.page_source)
    
def get_quora_data(lurl,browser):
   # try:
   		print lurl
   		browser.get(lurl)
   		y()
   		return parse(browser,browser.page_source)
   # except :
   		print 'error at url '+lurl

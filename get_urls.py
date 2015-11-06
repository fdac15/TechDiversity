import requests, json, sys, time, re
from bs4 import BeautifulSoup

beg_url = "http://dl.acm.org/"
list_url = "http://dl.acm.org/browse_by.cfm?by=title&pub=&type=thesis&preflayout=flat&CFID=722520619&CFTOKEN=62773377"

r = requests.get(list_url)

theses_list = open("theses_list.txt","w")

soup = BeautifulSoup(r.text, "html.parser")
for link in soup.findAll("a"):
	s = link.get("href")
	if s is not None and "citation" in s:
		print(beg_url + s)
		theses_list.write(beg_url + s + "\n")
theses_list.close()	

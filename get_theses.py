import requests, json, sys, time, re
from bs4 import BeautifulSoup
import time

head = {'User-Agent': 'Mozilla/5.0'}

f = open("theses_list.txt","r")
lines = f.read().splitlines()
f.close()

count = 1
start = time.time()
for url in lines:
	if count % 100 == 1:
		f.close()
		f = open("results" + str(count) + ".txt", "w")

	r = requests.get(url, headers=head)

	soup = BeautifulSoup(r.text, "html.parser")

	if r.status_code == 403:
		print("error code 403")
		break

	title = soup.find("meta", {"name":"citation_title"})['content']
	author = soup.find("meta", {"name":"citation_authors"})['content']
	uni = soup.find("meta", {"name":"citation_publisher"})['content']
	date = soup.find("meta", {"name":"citation_date"})['content']
	isbn = ""
	if soup.find("meta", {"name":"citation_isbn"}):
		isbn = soup.find("meta", {"name":"citation_isbn"})['content']

	f.write("thesis no: " + str(count) + "\n")
	f.write("title: " + title + "\n")
	f.write("author: " + author + "\n")
	f.write("uni: " + uni + "\n")
	f.write("date: " + date + "\n")
	f.write("isbn: " + isbn + "\n\n")

	print(str(count) + ":  " + title)

	count += 1
f.close()

end = time.time()
elapsed = end - start
print("time elapsed = " + str(elapsed))

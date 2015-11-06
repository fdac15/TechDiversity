import pymongo, json

s = open("acm_final_results","r")
lines = s.read().splitlines()
s.close()

client = pymongo.MongoClient(host="da0.eecs.utk.edu")
db = client["TechDiversity"]
coll = db["acm"]

for line in lines:
	words = line.split()
	if words:
		if words[0] == "title:":
			title = ' '.join(words[1:len(words)])
		if words[0] == "author:":
			author = ' '.join(words[1:len(words)])
		if words[0] == "uni:":
			uni = ' '.join(words[1:len(words)])
		if words[0] == "date:":
			date = words[1]
		if words[0] == "isbn:":
			if len(words) == 2:
				isbn = words[1]
			else:
				isbn = ""
			posts = {
				"title" : title,
				"author" : author,
				"university" : uni,
				"date" : date,
				"isbn" : isbn
			}
			coll.insert(posts)
			print("inserting " + author)

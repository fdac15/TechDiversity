import pymongo, json, operator

client = pymongo.MongoClient(host="da0.eecs.utk.edu")
db = client["TechDiversity"]
coll = db["acm"]

count = 0
r = coll.find({})
d = {}
for rec in r:
	uni = rec['university']
	if uni in d:
		d[uni] += 1
	else:
		d[uni] = 1
sorted_d = sorted(d.items(), key = operator.itemgetter(1))
sorted_d_rev = sorted_d.reverse()

for i in range(0,50):
	print(sorted_d[i])

print(d['University of Tennessee'])

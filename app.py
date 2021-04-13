import datetime
import random
import re
from pymongo import MongoClient
from bson import ObjectId
from faker import Faker
from flask import Flask, render_template, request


# fake = Faker() 
app = Flask(__name__)

list_collections=[]

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	if request.method == 'POST':
		global list_collections 
		email = request.form['email']
		collection = re.sub(r"[@.]", "", email)
		print(collection)
		password = request.form['pass']
		print(password)

		client = MongoClient('localhost', 27017)
		db = client["crm_kvant"]

		users = db[collection]
		users.insert_one({ 
			"username" : "person_greg",
		        "name" : "Michael Rodriguez",
		        "mail" : email,
		        "password": password,
		        "datetime" : "2021-04-06T11:37:58.786Z"})
		list_collections = db.collection_names()
		print(list_collections)	
	return render_template('index.html')




if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

# def gen_data():
# 	for _ in range(20):
# 		user = fake.profile()
# 		dict_user={
# 		'username': user['username'], 
# 		'name': user['name'], 
# 		'mail': user['mail'],
# 		'datetime': datetime.datetime.utcnow() }
# 		lst_user.append(dict_user)
		#print(lst_user)

	# users.insert_many(lst_user)

# users.insert_one({
# 	"username" : "person_greg",
#     "name" : "Michael Rodriguez",
#     "mail" : "andrewsalazar@hotmail.com",
#     "datetime" : "2021-04-06T11:37:58.786Z"})

# users.insert_one({ 
# 	"username" : "person_greg",
#         "name" : "Michael Rodriguez",
#         "mail" : "andrewsalazar@hotmail.com",
#         "datetime" : "2021-04-06T11:37:58.786Z"})

# users.insert_one({"username" : "shelbyjones",
#         "name" : "Michael Rodriguez",
#         "mail" : "melaniemckay@gmail.com",
#         "datetime" : "2021-04-06T11:37:58.787Z"})

# person = users.update_many({"name":"Michael Rodriguez"},{"$push":{"cost":random.randint(1,20)}})
#for person in users.find({"name":"Michael Rodriguez","cost":{"$gte":10, "$lte":15}}):	print(person)
#	print("\n\n")



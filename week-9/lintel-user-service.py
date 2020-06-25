# ============================================
# ; Title:  lintel_user-service.py
# ; Author: Professor Krasso
# ; Date:   22 June 2020
# ; Modified by: Jeff Lintel
# ; Description: demonstrate adding a user to
# ; MongoDB with Python
# ===========================================

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

user = {
    "first_name": "Melissa",
    "last_name": "Mendelson",
    "email": "m.mendelson@example.org",
    "employee_id": "2581478",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

employee_id = "2581478"

pprint.pprint(db.users.find_one({"employee_id": employee_id}))
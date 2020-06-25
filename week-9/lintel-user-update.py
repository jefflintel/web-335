# ==============================================
# ; Title:  lintel_user-update.py
# ; Author: Professor Krasso
# ; Date:   22 June 2020
# ; Modified by: Jeff Lintel
# ; Description: demonstrate updating a user in
# ; MongoDB with Python
# ==============================================

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

db.users.update_one(
    {"employee_id": "2581478"},

    { 
        "$set": {
        "email": "jlintel@my365.bellevue.edu"
    }
  }
)


pprint.pprint(db.users.find_one({"employee_id": "2581478"}, {"_id": 0, "email": 1, "employee_id": 1, "first_name": 1, "last_name": 1}))
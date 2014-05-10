from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
MONGO_HOSTNMAME = 'localhost'
MONGO_PORT = 27017

client = MongoClient(MONGO_HOSTNMAME, MONGO_PORT)
db = client.zapas

import zapas.views
print 'call'
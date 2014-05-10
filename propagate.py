from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017) 

db = client.zapas
valves = db.valves

for valve_number in range(1, 20):
    valve = {'valve_id': valve_number, 
             'valve_name': valve_number,
             'valve_state': True}
    valves.insert(valve)
    

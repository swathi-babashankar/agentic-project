import json

with open('data.json') as f:
    data = json.load(f)
print(data['buildings'])

def getAvailableRooms(building_data):
   return building_data.get('buildings', [])

def getGRooms(building_data):
    return building_data.get('buildings', [])[0].get('blocks', {}).get('G-Block', {})


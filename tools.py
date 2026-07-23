import json
# Importing the JSON file and loading the data.
with open('data.json') as f:
    data = json.load(f)
# print(data['buildings'])

# Function to get all the available rooms from the building data.
def getAvailableRooms(building_data):
   return building_data.get('buildings', [])
   
# Function to get the G-Block rooms from the building data.
def getGRooms(building_data):
    return building_data.get('buildings', [])[0].get('blocks', {}).get('G-Block', {})


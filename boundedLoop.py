from tools import getAvailableRooms, getGRooms
from config import allowed_tools, trace, MAX_STEPS
import json

# Importing the JSON file and loading the data.
with open('data.json') as f:
    data = json.load(f)

# allowed tools
# let the agent choose which tool to use based on the request type
trace.append(f"Allowed tools: {allowed_tools}")
trace.append(f"Max steps: {MAX_STEPS}")


def runLoop(requestType, building_data):
    availableRooms = []
    # if request type is in allowed tools, then tool = tool of request type(MAYBE TRY )
    for step in range(MAX_STEPS):
        if requestType == "Get available rooms":
            tool = getAvailableRooms
            trace.append(f"Tool selected: {tool.__name__}")
            
        elif requestType == "Get available rooms in G block":
            tool = getGRooms
            trace.append(f"Tool selected: {tool.__name__}")
            
        elif requestType not in allowed_tools:
            print(f"Tool {requestType} is invalid.")
            trace.append(f"Invalid tool: {requestType}")
            return "ESCALATE"

        # If the tool is not allowed, 
        # it prints an error message and returns "ESCALATE".

# Agent chooses the tool based on the request type and calls it to get the available rooms.
#  The results are then printed and returned as "COMPLETE". 
        availableRooms.extend(tool(building_data))
        print("rooms", availableRooms)
        print("trace", trace)
        return "COMPLETE"

runLoop("Get available rooms in G block", data)

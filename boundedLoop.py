from tools import choose_tool, get_available_dates
from config import allowed_tools, trace, MAX_STEPS
import json

# Importing the JSON file and loading the data.
with open('data.json') as f:
    data = json.load(f)

# Tracing the allowed tools and maximum steps for debugging purposes.
trace.append(f"Allowed tools: {allowed_tools}")
trace.append(f"Max steps: {MAX_STEPS}")


def runLoop(requestType, building_data, date):
    availableRooms = []

    for step in range(1, MAX_STEPS + 1):
        trace.append(f"Step {step}: evaluating request '{requestType}'")

        print("date", date)
        requestType = get_available_dates(date)
        tool = choose_tool(requestType)
        
        if tool is None:
            print(f"Tool {requestType} is invalid.")
            trace.append(f"Invalid tool: {requestType}")
            return "ESCALATE"

        trace.append(f"Tool selected: {tool.__name__}")
        trace.append(f"Date selected: {date}")

        result = tool(building_data)
        if isinstance(result, list):
            availableRooms.extend(result)
        else:
            availableRooms.append(result)

        print("rooms", availableRooms)
        print("trace", trace)
        # return "COMPLETE"


if __name__ == "__main__":
    runLoop("Get available rooms", data, "2026-07-04")

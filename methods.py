import json

def readDept():
    try:
        with open("departments.json","r") as file:
            departments = json.load(file)
            return departments
    except FileNotFoundError:
        return {}
    



def addDept():
    try:
        with open("departments.json","w") as file:
            departments = json.load(file)
            return departments
    except FileNotFoundError:
        return {}



    
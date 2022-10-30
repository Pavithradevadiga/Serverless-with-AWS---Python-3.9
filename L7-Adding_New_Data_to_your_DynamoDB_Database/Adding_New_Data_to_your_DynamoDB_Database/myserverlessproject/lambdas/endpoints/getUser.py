import json
from lambdas import API_Responses as response

data = {
        "1234" : {'name': 'Anna Jones','age': 25, 'job': 'journalist'},
        "7893" : {'name': 'Chris Smith','age': 52, 'job': 'teacher'},
        "5132" : {'name': 'Tom Hague','age': 23, 'job': 'plasterer'}
    }

def handler(event, context):
    print("event",event)

    if not event["pathParameters"] or not event["pathParameters"]["ID"]:
        return response._400({'message': 'missing the ID from the path'})

    ID = event["pathParameters"]["ID"]

    if ID in data:
        return response._200(data[ID])   

    return response._400({'message': 'no ID in data'}) 


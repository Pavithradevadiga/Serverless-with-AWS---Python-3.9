import json
from lambdas.common import API_Responses as response
from lambdas.common import Dynamo 
import os

data = {
        "1234" : {'name': 'Anna Jones','age': 25, 'job': 'journalist'},
        "7893" : {'name': 'Chris Smith','age': 52, 'job': 'teacher'},
        "5132" : {'name': 'Tom Hague','age': 23, 'job': 'plasterer'}
    }
tableName= os.environ.get('tableName')

def handler(event, context):
    print("event",event)

    if not event["pathParameters"] or not event["pathParameters"]["ID"]:
        return response._400({'message': 'missing the ID from the path'})

    ID = event["pathParameters"]["ID"]

    user =  Dynamo.get(ID,tableName)

    if not user:
        return response._400({'message': 'Failed to get user by ID'})
    
    return response._200({user})
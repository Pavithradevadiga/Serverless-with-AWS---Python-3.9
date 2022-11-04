from lambdas.common import API_Responses as response
from lambdas.common import Dynamo
import os

tableName = os.environ.get('tableName')

def handler(event, context):
    print(event)
    connection = {}
    

    connection['ID'] = event['requestContext']['connectionId']
    Dynamo.delete(connection['ID'],tableName)

    return response._200({'message': 'disconnected'})
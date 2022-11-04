from lambdas.common import API_Responses as response
from datetime import datetime
from lambdas.common import Dynamo
import os

tableName = os.environ.get('tableName')

def handler(event, context):
    print(event)

    connection = {}
    

    connection['ID'] = event['requestContext']['connectionId']
    connection['domainName'] = event['requestContext']['domainName']
    connection['stage'] = event['requestContext']['stage']
    
    connection['date'] = str(datetime.timestamp(datetime.now()))
    connection['messages'] = []
    print('connection',connection)

    Dynamo.write(connection,tableName)

    return response._200({'message': 'connected'})
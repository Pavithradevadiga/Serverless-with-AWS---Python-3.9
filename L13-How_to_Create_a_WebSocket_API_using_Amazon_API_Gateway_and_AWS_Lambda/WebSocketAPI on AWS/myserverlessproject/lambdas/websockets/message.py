from lambdas.common import API_Responses as response
import json
from lambdas.common import Dynamo
from lambdas.common import websocketMessage as WebSocket
import os

tableName = os.environ.get('tableName')
def handler(event, context):
    print(event)

    connection = {}

    connection['ID'] = event['requestContext']['connectionId']
    body = json.loads(event['body'])
    print(body['message'])
    try:

        record = Dynamo.get(connection['ID'],tableName)
        messages = record['messages']
        stage = record['stage']
        domainName = record['domainName']

        messages.append(body['message'])   
        record['messages'] = messages
        print(record)
        data = record
        
        Dynamo.write(data,tableName)

        WebSocket.send(domainName,stage,connection['ID'],'This is a reply to your message')

        return response._200({'message': 'got a message'})
    except Exception as ex:
        print('exception ocurred',ex)
        return response._400({'message': 'message could not be received'})    

    return response._200({'message': 'got a message'})
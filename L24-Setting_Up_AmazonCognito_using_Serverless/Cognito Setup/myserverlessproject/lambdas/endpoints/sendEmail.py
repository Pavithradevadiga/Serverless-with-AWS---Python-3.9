import json
from lambdas.common import API_Responses as response
import boto3

client = boto3.client('ses')

def handler(event, context):
    print("event",event)

    data = {}

    body = json.loads(event['body'])
    print(body)


    data['to'] = body['to']
    data['from'] = body['from']
    data['subject'] = body['subject']
    data['text'] = body['text']

    if not data['to'] or not data['from'] or not data['subject'] or not data['text']:
        response._400({'message': 'to,from,subject and text are all required in the body'})

    try:
        Response = client.send_email(
            Source = data['from'],
            Destination = {
            'ToAddresses': [
                data['to'],
            ]},
            Message = {
            'Subject': {
                'Data': data['subject'],
            },
            'Body': {
                'Text': {
                    'Data': data['text'],
                }
            }
            }
        )
        return response._200({}) 
    except Exception as ex:
        print('error sending email',ex)
        return response._400({'message': 'The email failed to send'})

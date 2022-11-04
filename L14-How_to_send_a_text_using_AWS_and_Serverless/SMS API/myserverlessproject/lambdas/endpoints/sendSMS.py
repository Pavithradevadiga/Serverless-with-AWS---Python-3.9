import json
from lambdas.common import API_Responses as response
import boto3

client = boto3.client('sns')

def handler(event, context):
    print(event)

    body = json.loads(event["body"])

    if not body or not body["phoneNumber"] or not body['message']:
        return response._400({'message':'missing phone number or message from the body'})

    
    try:
        client.set_sms_attributes(
        attributes={
            'DefaultSMSType': 'Transactional'
        }
        ) 

        client.publish(
            PhoneNumber = body['phoneNumber'],
            Message = body['message']
        )
    except Exception as ex:
        print('Exception ocurred',ex) 
        return response._400({'message':'text failed to send'})   

    return response._200({'message': 'text has been sent'})
import json
from lambdas.common import API_Responses as response
import boto3

client = boto3.client('comprehend')

def handler(event,context):
    body = json.loads(event['body'])

    if not body or not body['text']:
        return response._400({'message': 'no text field on the body'})


    text = body['text']

    try:
        entityResults = client.batch_detect_entities(
        TextList = [text],
        LanguageCode = 'en'
        )
        print(entityResults)
        entities = entityResults['ResultList'][0]

        sentimentResults = client.batch_detect_sentiment(
        TextList = [text],
        LanguageCode = 'en'
        )
        sentiment = sentimentResults['ResultList'][0]
        
        print('entities',entities)
        print('sentiment',sentiment)
        responseData = {
            'entities': entities,
            'sentiment' : sentiment
        }
        print(responseData)

        return response._200(responseData)

    except Exception as ex:
        print('exception',ex) 
        return response._400({'response':'failed to work with comprehend'})   

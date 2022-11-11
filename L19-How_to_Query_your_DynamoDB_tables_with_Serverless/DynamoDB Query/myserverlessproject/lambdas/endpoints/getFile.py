import json
from lambdas.common import API_Responses as response
from lambdas.common import S3 
import os


bucket = os.environ.get('bucketName')

def handler(event, context):
    print("event",event)

    if not event["pathParameters"] or not event["pathParameters"]["fileName"]:
        return response._400({'message': 'missing the fileName from the path'})

    fileName = event["pathParameters"]["fileName"]

   
    
    try:
        file = S3.get(fileName,bucket)
    except Exception as ex:
        file = None
        print('error in S3 get',ex) 


    if not file:
        return response._400({'message': 'Failed to read the data by fileName'})
    
    return response._200(file)
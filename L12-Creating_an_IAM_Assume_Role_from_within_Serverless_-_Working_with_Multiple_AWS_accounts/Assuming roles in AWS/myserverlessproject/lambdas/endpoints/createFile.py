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

    data = json.loads(event["body"])
    
    try:
        newData = S3.write(data,fileName,bucket)
    except Exception as ex:
        newData = None
        print('exception occurred',ex) 


    if not newData:
        return response._400({'message': 'Failed to write data by fileName'})
    
    return response._200(newData)
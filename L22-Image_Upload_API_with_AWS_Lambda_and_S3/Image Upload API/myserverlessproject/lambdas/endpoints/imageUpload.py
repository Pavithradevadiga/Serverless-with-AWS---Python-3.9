import json
from lambdas.common import API_Responses as response
from base64 import b64encode,b64decode
import filetype
import uuid
import boto3
import os
from mimetypes import guess_extension, guess_type

client = boto3.client('s3')
s3 = boto3.resource('s3')

allowedMimes = ['image/jpeg','image/png','image/jpg']

def handler(event,context):
    try:
        body = json.loads(event["body"])
        print(body)

        if not body or not body["image"] or not body["mime"]:
            return response._400({'message' : 'incorrect body on request'})

        if body["mime"] not in allowedMimes:
            return response._400({'message' : 'mime is not allowed'})

        imageData = body["image"]

        if body["image"][0:7] == 'base64,':
            print('slicing')
            imageData =  body["image"][7:len(body["image"])]
 
        dec = b64decode(imageData)
        
        fileinfo = filetype.guess(dec)
        detectedExt = fileinfo.extension
        detectedmime = fileinfo.mime


        if detectedmime != body["mime"]:
            return response._400({'message':"mime type don't match"})

        name = str(uuid.uuid4())
        key = name+'.'+detectedExt

        print('writing image to bucket called '+key)
        
        putobject = client.put_object(
            Body = dec,
            Key = key,
            ContentType = body["mime"],
            Bucket = os.environ.get('imageUploadBucket'),
            ACL = 'public-read'
        )

        url = 'https://'+os.environ.get('imageUploadBucket')+'.s3.amazonaws.com/'+key
        print(url)
        return response._200({
            'imageURL': url
        })
    except Exception as ex:
        print('Exception ocurred',ex)
        return response._400({'message': ex})
        

import boto3
import json
import mimetypes
import base64 

s3Client = boto3.client('s3')

def get(fileName,bucket):
    data = s3Client.get_object(
        Bucket = bucket,
        Key = fileName
    )

    if not data:
        raise Exception(f"Failed to get file {fileName}, from {bucket}")

    if fileName[-4:] == 'json':
        data = json.dumps(data)
        data = data['Body'].read().decode("utf-8")
        data = str(data)
        
    print('raw data',data)
    data = data['Body'].read()     

    return data     

def write(data,fileName,bucket,ACL,ContentType):
    response = s3Client.put_object(
        Body = data if type(data) is bytes else json.loads(data),
        Bucket = bucket,
        Key = fileName,
        ACL = ACL,
        ContentType = ContentType
    )

    if not response:
        raise Exception(f"There was an error writing the file")

    return response    
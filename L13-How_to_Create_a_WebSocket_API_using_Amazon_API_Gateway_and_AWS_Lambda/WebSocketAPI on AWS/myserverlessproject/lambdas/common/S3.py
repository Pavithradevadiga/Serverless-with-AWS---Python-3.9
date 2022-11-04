import boto3
import json

s3Client = boto3.client('s3')

def get(fileName,bucket):
    data = s3Client.get_object(
        Bucket = bucket,
        Key = fileName
    )

    if not data:
        raise Exception(f"Failed to get file {fileName}, from {bucket}")

    if fileName[-4:] == 'json':
        print('yoyoy')
        # data = json.dumps(data)
        data = data['Body'].read().decode("utf-8")
        data = str(data)

    return data     

def write(data,fileName,bucket):
    response = s3Client.put_object(
        Body = json.dumps(data),
        Bucket =  bucket,
        Key = fileName
    )

    if not response:
        raise Exception(f"There was an error writing the file")

    return response    
from distutils.log import error
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')


def get(ID,tableName):
    tablename = dynamodb.Table(tableName)
    data = tablename.get_item(Key={'ID':ID})

    try:
        print(data['Item'])
        return data["Item"]
    except Exception as ex:
        print('exception occurred',ex) 
        raise Exception(f"There was an error fetching the data for ID of {ID} from {tableName}")

def write(data,tableName):
    tablename = dynamodb.Table(tableName)
    if data["ID"]:

        try:
            response = tablename.put_item(Item = data)
            return data
        except Exception as ex: 
            raise Exception(f"There was an error inserting  ID of {data.ID} from {tableName}")

    else:
        raise Exception("no ID on the data") 

def update(tableName,primaryKey, primaryKeyValue, UpdateKey, UpdateValue):
    tablename = dynamodb.Table(tableName) 

    try:
        response = tablename.update_item(Key={primaryKey: primaryKeyValue},
                    UpdateExpression="set "+UpdateKey+"=:r",
                    ExpressionAttributeValues={
                    ':r': UpdateValue},
                    ReturnValues="UPDATED_NEW") 
    except Exception as ex:   
        print('Exception ocurred',ex)

def query(tableName,index,queryKey,queryValue):
    tablename = dynamodb.Table(tableName) 

    try:
        print('inside try of query')
        response = tablename.query(
        IndexName = index,
        KeyConditionExpression = Key(queryKey).eq(queryValue)
        )   
        
        if response['Items'] is None:
            response['Items'] = []

        return response['Items']    
    except Exception as ex:
        print('Exception ocurred',ex)

from distutils.log import error
import boto3

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
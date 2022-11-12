from lambdas.common import Dynamo 
import os

tableName = os.environ.get('signupTableName')


def handler(event,context):
    print(event)

    ID = event["Input"]["Payload"]["ID"]

    try:
        row = Dynamo.get(ID,tableName)
        return row
    except Exception as ex:
        print('Exception ocurred',ex)    
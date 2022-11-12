from lambdas.common import Dynamo 
import os
import random

tableName = os.environ.get('signupTableName')


def handler(event,context):
    print(event)

    email = event["Input"]["signup"]["email"]
    ID = str(random.randint(0,10))
    data = {}
    data['email'] = email
    data['ID'] = ID
    data['played'] = 'false'
    
    try:
        response = Dynamo.write(data,tableName)

        return response
    except Exception as ex:
        raise Exception('Exception ocurred',ex)    
import json
import os
from lambdas.common import API_Responses as response
from lambdas.common import Dynamo 

tableName = os.environ.get('tableName')

def handler(event, context):
    print("event",event)

    if not event["pathParameters"] or not event["pathParameters"]["game"]:
        return response._400({'message': 'missing the game from the path'})

    game = event["pathParameters"]["game"]
    print(game)
    gamePlayers = Dynamo.query(tableName,'game-index','game',game)

    # try:
    #     user =  Dynamo.get(game,tableName)
    # except Exception as ex:
    #     user = None
    #     print('exception occurred',ex)    

    # if not user:
    #     return response._400({'message': 'Failed to get user by game'})
    
    return response._200(gamePlayers)
import json
from lambdas.common import API_Responses as response


def handler(event, context):
    print("event",event)

    
    return response._200()   

    


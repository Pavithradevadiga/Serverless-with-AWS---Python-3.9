import json

def _200(data = None):
    if data is None:
        data = {}

    return{
        "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Origin': '*'
        },
        "statusCode": 200,
        "body": json.dumps(data)
    } 

def _400(data = None):
    if data is None:
        data = {}

    return{
        "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Origin': '*'
        },
        "statusCode": 400,
        "body": json.dumps(data)
    }         
from lambdas.common import API_Responses as response

def handler(event, context):
    print(event)

    return response._200({'message': 'default'})
import boto3

def create(domainName,stage):
    print(type(domainName),type(stage))
    endpoint = 'https://'+domainName+'/'+stage
    print('endpoint',endpoint)

    client = boto3.client('apigatewaymanagementapi', endpoint_url=endpoint)
    return client

def send(domainName,stage,connectionID,message):
    ws = create(domainName,stage)

    response = ws.post_to_connection(
    Data = message,
    ConnectionId = connectionID
    )    

    return response
import boto3

client = boto3.client('ses')

def handler(event,context):
    print("event",event)
    email = event["Input"]["Payload"]["email"]

    message = """Hi,
    We saw that you signed up for our gaming platform but haven't played yet..
    We hope you play soon"""

    try:
        Response = client.send_email(
            Source = 'pavithradevadiga1@gmail.com',
            Destination = {
            'ToAddresses': [
                email,
            ]},
            Message = {
            'Subject': {
                'Data': 'Remember to use the gaming platform',
            },
            'Body': {
                'Text': {
                    'Data': message,
                }
            }
            }
        )
        
    except Exception as ex:
        raise Exception('error sending email',ex)
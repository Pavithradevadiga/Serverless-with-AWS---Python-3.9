import boto3
from lambdas.common import API_Responses as response
import requests

client = boto3.client('ses')
newsURL = 'https://newsapi.org'

def handler(event,context):

    techNews = getNews()

    emailHTML = createEmailHTML(techNews)

    try:    
        client.send_email(
        Destination={
        'ToAddresses': [
            'pavithradevadiga1@gmail.com'],
        },
        Message={
        'Subject': {
            'Data': 'Morning Tech Newzzz',
        },
        'Body': {
            'Html': {
                'Data': emailHTML,
            },
        }
        },
        Source='pavithradevadiga1@gmail.com'
        )
        response._200({'message':'email sent'})
    except Exception as ex:
        print('exception as',ex)
        return response._400({'message':'failed to send an email'})

    def createEmailHTML(techNews):
        return '''<html>
        <body>
            <h1>Top Tech News</h>
            '''+'yep'+'''</body></html>'''


    def getNews():
        params = {
            params: {
                'q': 'technology',
                'language': 'en'
            },
            'headers':{
                'X-Api-Key': '75f6cc0909cc43a5bfcfde4b1a35588a'
            }
        }
        newsData = requests.get(newsURL+'/v2/top-headlines',params)

        if not newsData:
            raise Exception('no data from news api')

        sliceObj = slice(0,1)
        newsDataLtd = newsData['articles'] 
        return newsDataLtd[sliceObj]    


        



        
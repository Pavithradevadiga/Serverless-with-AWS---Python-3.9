import boto3
from lambdas.common import API_Responses as response
import requests
import json

client = boto3.client('ses')
newsURL = 'https://newsapi.org'

def handler(event,context):
    
    def getNews():
        options = {
            'q': 'technology',
            'language': 'en'
          }
        
        newsData = requests.get(
          newsURL+'/v2/top-headlines',
          headers={"Authorization" : "75f6cc0909cc43a5bfcfde4b1a35588a"},
          params = options
        )
        # print(newsData.json())

        if not newsData.json():
            raise Exception('no data from news api')

        sliceObj = slice(0,5)
        newsDataLtd = newsData.json()['articles'] 
        # print('First 5 articles',newsDataLtd)
        return newsDataLtd[sliceObj]   
        
    def formatNews(article):
        articleFormatted = '<h3>'+article['title']+'</h3><p>'+article['description']+'</p>+<a href='+article['url']+'><button>Read More</button></a>'
        return articleFormatted   
        
        
    def createEmailHTML(techNews):
        frontpart = "<html><body><h1>Top Tech News</h1>"
        lastpart = "</body></html>"
        articles = ''
        for article in techNews:
            articles = articles+formatNews(article)
        finalformattedArticles = frontpart+articles+lastpart
        print(finalformattedArticles)
        return finalformattedArticles    
 

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

    


    

        



        
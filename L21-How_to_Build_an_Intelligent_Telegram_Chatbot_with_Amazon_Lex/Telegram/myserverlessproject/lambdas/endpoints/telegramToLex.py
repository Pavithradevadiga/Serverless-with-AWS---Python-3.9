import json
import boto3
from lambdas.common import API_Responses as response
import requests

client = boto3.client('lex-runtime')

def handler(event,context):
    try:
        body = json.loads(event["body"])
        print('body:',body)
        
        lexResponse = mapTelegramToLex(body) 
        print(lexResponse)
        messageForTelegram = mapLexToTelegram(lexResponse,body)
        print('messageForTelegram',messageForTelegram)
        requestResponse = sendToTelegram(messageForTelegram)
        
        print('sendToTelegram',requestResponse)

        return response._200()
    except Exception as ex:
        print('exception ocurred',ex)
        response._400()

def mapTelegramToLex(body):
    chatID = str(body["message"]["chat"]["id"]) 
    message = body["message"]["text"]
    response = client.post_text(botName='telegramBot',botAlias='dev',userId=chatID,sessionAttributes={},inputText=message)
    return response 

def  mapLexToTelegram(lexResponse,body):
    return {
        'text' : lexResponse["message"],
        "chat_id" : body["message"]["chat"]["id"]
    } 

def sendToTelegram(message):
    token = '5799062970:AAFUi-K8Pez7_ANwZg99Hcnhh7LrKfYBVeQ'
    telegramURL = 'https://api.telegram.org/bot'+token+'/sendMessage'

    response =  requests.post(telegramURL,message)  
    return response
import requests
import json
from domain import jsonMapper


class TransferService:
    def generateToken():

        url = 'https://api.sandbox.transferwise.tech/oauth/token'
        data = { 'grant_type': 'refresh_token',   
          'refresh_token': 'efd76f1c-f819-4138-b5f1-2fe69512cec7'}

# Set headers including authorization token and content type
        headers = {'Authorization': 'Basic dHctdGVzdC1iYW5rOnR3LXRlc3QtYmFuaw==',
           'Content-Type': 'application/x-www-form-urlencoded'}

# Make the POST request
        response = requests.post(url, headers=headers, data=data)
        print(response.json())

# Check the response status code and content


    def createQuote(createQuoteRequest):
        data = createQuoteRequest.__dict__
        print(data)
        json_string = json.dumps(data)
        print(json_string)
        url = "https://api.sandbox.transferwise.tech/v2/quotes"
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer 3978c03a-3165-444e-8a7f-c10f6b4a3a21'}
        
        response = requests.post(url, data=json_string, headers=headers)
        print(response)
        return response.json()

    
    def createRecipient(createRecipientRequest):
        data = jsonMapper.to_api_data(createRecipientRequest)
        json_string = json.dumps(data)
        print(data)
        print(json_string)
        url = "https://api.sandbox.transferwise.tech/v1/accounts"
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer 3978c03a-3165-444e-8a7f-c10f6b4a3a21'}

        response = requests.post(url, data=json_string, headers=headers)
        print(response)
        return response
    
    
    

      

 


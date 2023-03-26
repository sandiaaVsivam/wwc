import requests
import json
from domain import jsonMapper


class TransferService:
    def generateToken(self):

        url = 'https://api.sandbox.transferwise.tech/oauth/token'
        data = { 'grant_type': 'refresh_token',   
          'refresh_token': '<>'}

# Set headers including authorization token and content type
        headers = {'Authorization': 'Basic <>',
           'Content-Type': 'application/x-www-form-urlencoded'}

# Make the POST request
        response = requests.post(url, headers=headers, data=data)
        print(response.json())

# Check the response status code and content


    def createQuote(createQuoteRequest):
        print(vars(createQuoteRequest))
        json_string = json.dumps(vars(createQuoteRequest))
        print(json_string)
        url = "https://api.sandbox.transferwise.tech/v2/quotes"
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer '}
        
        response = requests.post(url, data=json_string, headers=headers)
        print(response)
        return response.json()

    
    def createRecipient(createRecipientRequest):
        data = jsonMapper.to_api_data(createRecipientRequest)
        json_string = json.dumps(data, default=lambda o: vars(o))
        print(data)
        print(json_string)
        url = "https://api.sandbox.transferwise.tech/v1/accounts"
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer '}

        response = requests.post(url, data=json_string, headers=headers)
        print(response)
        return response
    
    
    

      

 


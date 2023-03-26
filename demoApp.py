
from domain import CreateQuoteRequest, CreateRecipientRequest, RecipientAccountDetails, Address
from service import transferService

class DemoApplication:
    def main(self):
        # transferService.TransferService.generateToken()
        createQuoteRequest = self.getQuoteRequest()
        response = transferService.TransferService.createQuote(createQuoteRequest)
        if(response == None) :
            print("Quote creation failed")
        else:
            print("Created quote id ",response["id"])

        self.createRecipient(createQuoteRequest._sourceCurrency)

    def getQuoteRequest(self):
        sourceCurrency = input("From which currency would you like to transfer? Please enter the currency code. (e.g., GBP)")
        targetCurrency = input("What currency do you want to transfer to (EUR)?")
        sourceAmount = input("How much would you like to transfer? Please enter the amount in numbers (up to 50,000).")
        print("Creating a quote...")
        quote = CreateQuoteRequest.CreateQuoteRequest()
        quote._sourceCurrency = sourceCurrency
        quote._targetCurrency= targetCurrency
        quote._sourceAmount = sourceAmount
        return quote
    

    def createRecipient(self, sourceCurrency):
        print("Please enter recipient account details:")
        accountNumber = input("Account number")
        email = input("Email")
        accountType = input("Account type:(eg CHECKING)")
        print("Creating sender account...")
        recipient = CreateRecipientRequest.CreateRecipientRequest()
        recipient._currency = sourceCurrency
        recipient._type = accountType
        recipient._accountHolderName = "Sender Account"
        details = RecipientAccountDetails.RecipientAccountDetails()
        details._accountNumber = accountNumber
        details._email=email
        details._accountType=accountType
        details._address=Address.Address()
        recipient._details=details
        response = transferService.TransferService.createRecipient(recipient)
        if(response != None):
            print("SUCCESSFUL!")


bb = DemoApplication()
bb.main()




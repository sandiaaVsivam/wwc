from domain import SenderAccountDetails

class CreateSenderAcctRequest:
     def __init__(self, accountHolderName, currency, type):
          self.__accountHolderName = accountHolderName
          self.__currency = currency
          self.__type = type
          self.__details = SenderAccountDetails()
          self.__profile = 16727665



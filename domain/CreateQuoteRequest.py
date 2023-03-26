from domain import metaClass

class CreateQuoteRequest(metaclass=metaClass.AutoGetSet):
    _attributes = ['sourceCurrency', 'targetCurrency', 'targetAmount', 'sourceAmount', 'profile']
    def __init__(self):
        self._sourceCurrency = None
        self._targetCurrency = None
        self._targetAmount = None
        self._sourceAmount = None
        self._profile = 16727665

  
    
   
        

    
  

    
    
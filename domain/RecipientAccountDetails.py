from domain import Address, metaClass

class RecipientAccountDetails(metaclass = metaClass.AutoGetSet):
        _attributes = ['legalType', 'accountType', 'email', 'accountType', 'address', 'abartn', 'accountNumber']

        def __init__(self):
            self._legalType = "PRIVATE"
            self._accountType = None
            self._email = None
            self._address = Address.Address()
            self._abartn = "064000020"
            self._accountNumber = None

     


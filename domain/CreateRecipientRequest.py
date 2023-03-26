from domain import RecipientAccountDetails, metaClass

class CreateRecipientRequest(metaclass=metaClass.AutoGetSet):
    _attributes = ['accountHolderName', 'currency', 'type', 'details']

    def __init__(self):
        self._accountHolderName = None
        self._currency = None
        self._type = None
        self._details = RecipientAccountDetails.RecipientAccountDetails()

    def to_dict(self):
        return self.__dict__
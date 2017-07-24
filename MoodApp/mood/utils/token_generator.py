from django.utils.crypto import get_random_string

class Token:
    """ Optionally change token length at initialization from default 32 """
    def __init__(self, length=32):
        self.length = length

    """ Generate a random token of a given length """
    def getToken(self):
        return get_random_string(length = self.length)



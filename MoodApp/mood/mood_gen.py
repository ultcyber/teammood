from utils.token_generator import Token
from models import Mood
from datetime import datetime

class MoodGen():

    def __init__(self, number_of_tokens):
        # Internal fields
        self.result = ""
        self.exception_list = []
        self.token = Token()

        # Processing moods
        self.token_num = number_of_tokens
        self.token_list = []
        self.__genTokens()
        self.__createMoods()

    """ Generate a random token list of given length """
    def __genTokens():
        for i in range(number_of_tokens):
            self.token_list.append(token.getToken())

    """
    Updates the mood table with the generated token list.
    Account for possible repetitions in uuids.
    """
    def __createMoods():
        current_tokens = list(token_list)
        while (current_tokens):
            try:
                Mood.objects.get(id=current_tokens[0])
                self.exception_list.append("ERROR: Mood uuid {} already exists".format(tk))
                current_tokens.remove(tk)
                current_tokens.append(token.getToken())
            except:
                # TODO: finish up model fields assignment
                Mood(id=token, date=datetime.now(), answered=false)
                current_tokens.remove(tk)

    def get_token_list():
        return self.token_list

    def get_result():
        self.result = "500" if len(self.exception) else "201"
        return self.result

    def get_exceptions():
        return self.exceptions

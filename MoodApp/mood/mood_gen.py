from .utils.token_generator import Token
from mood.models import Mood, Team
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

class MoodGen():
    """
    Mood generation class.

    Will generate a defined number of tokens and creates moods for current date.
    """
    def __init__(self, number_of_tokens, commit=True):
        """
        Generates a new MoodGen object

        Args:
            number_of_tokens (int): Number of tokens that will be generated and commited to the database
            commit (bool): whether to commit new tokens to the database. Defaults to True.
        """
        # Internal fields
        self.result = ""
        self.exception_list = []
        self.token = Token()
        self.commit = commit
        self.number_of_tokens = number_of_tokens
        self.token_list = []

        # Processing moods
        self.__genTokens()
        self.__createMoods()

    def __genTokens(self):
        # Generate a random token list of given length
        for i in range(self.number_of_tokens):
            self.token_list.append(self.token.getToken())

    def __createMoods(self):
        #  Updates the mood table with the generated token list. Account for possible repetitions in uuids.
        current_tokens = list(self.token_list)
        while (current_tokens):
            try:
                tk = current_tokens.pop()
                Mood.objects.get(uid=tk)
                current_tokens.append(self.token.getToken())
            except ObjectDoesNotExist:
                if self.commit:
                    try:
                        Mood(uid=tk, date_requested=datetime.now(), answered=false, team=Team(), comment="")
                    except:
                        self.exception_list.append("Error while creating a new mood object. Object uid {}".format(tk))

    def get_token_list(self):
        """
        Returns the list of currently generated tokens

        Returns:
        list: list of generated tokens
        """
        return self.token_list

    def get_result(self):
        """
        Returns the result of mood generation

        Returns:
            bool: result of the operation
        """
        self.result = True if len(self.exception_list) == len(self.token_list) else False
        return self.result

    def get_exceptions(self):
        """
        Returns the list of exceptions.

        Returns:
            list: exception list
        """
        return self.exceptions

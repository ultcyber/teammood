from utils.token_generator import Token
from models import Mood
from datetime import datetime

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

        # Processing moods
        self.token_num = number_of_tokens
        self.token_list = []
        self.__genTokens()
        self.__createMoods()

    def __genTokens():
        # Generate a random token list of given length
        for i in range(number_of_tokens):
            self.token_list.append(token.getToken())

    def __createMoods():
        #  Updates the mood table with the generated token list. Account for possible repetitions in uuids.
        current_tokens = list(token_list)
        while (current_tokens):
            try:
                Mood.objects.get(id=current_tokens[0])
                current_tokens.remove(tk)
                current_tokens.append(token.getToken())
            except:
                try:
                    if commit:
                        # TODO: finish up model fields assignment
                        Mood(id=token, date=datetime.now(), answered=false)
                    current_tokens.remove(tk)
                except:
                    self.exception_list.append("Error while creating a new mood object. Object uid {}".format(tk))

    def get_token_list():
        """
        Returns the list of currently generated tokens

        Returns:
        list: list of generated tokens
        """
        return self.token_list

    def get_result():
        """
        Returns the result of mood generation

        Returns:
            bool: result of the operation
        """
        self.result = True if len(self.exception_list) == len(self.token_list) else False
        return self.result

    def get_exceptions():
        """
        Returns the list of exceptions.

        Returns:
            list: exception list
        """
        return self.exceptions

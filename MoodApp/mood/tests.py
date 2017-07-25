from django.test import TestCase
from mood.models import Mood, Team
from mood.mood_gen import MoodGen

class MoodGenTests(TestCase):

    def test_I_can_generate_ten_moods(self):
        self.assertEqual(len(MoodGen(10, False).get_token_list()), 10)

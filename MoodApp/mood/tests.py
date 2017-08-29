from django.test import TransactionTestCase
from django.test import TestCase
from mood.models import Mood, Team
from mood.mood_gen import MoodGen
from django.utils import timezone
from django.test import Client
from django.core.exceptions import ObjectDoesNotExist
import datetime

import traceback

class MoodGenTests(TransactionTestCase):

    def setUp(self):
        self.test_team = Team.objects.create(name="Test Team")

    def test_I_can_generate_ten_moods(self):
        self.assertEqual(len(MoodGen(10, self.test_team, False).get_token_list()), 10)

    def test_I_can_generate_ten_moods_and_retrieve_them_from_db(self):
        moods = MoodGen(10, self.test_team)
        tokens = moods.get_token_list()
        failed_queries = []


        for token in tokens:
            try:
                mood = Mood.objects.get(uid=token)
            except ObjectDoesNotExist:
                print(">>>>> traceback <<<<<<")
                traceback.print_exc()
                print(">> end of traceback <<")
                failed_queries.append(token)

        self.assertEqual(len(failed_queries), 0)


    def test_generated_mood_has_right_default_values(self):
        moods = MoodGen(1, self.test_team)
        tokens = moods.get_token_list()
        token = tokens[0]

        try :
            mood = Mood.objects.get(uid=token)
        except ObjectDoesNotExist:
            traceback.print_exc()


        results = [
                mood.date_requested.month == timezone.datetime.now().month,
                mood.date_requested.day == timezone.datetime.now().day,
                mood.date_requested.year == timezone.datetime.now().year,
                mood.answered == False,
                ]

        self.assertNotIn(False,results,msg="Wrong default values for one of the fields")

class ViewsTests(TestCase):

    def test_I_get_404_when_trying_to_open_inexisting_token(self):
        client = Client()
        response = client.get("/mood/12345678901234567890123456789012")
        self.assertEqual(response.status_code, 404)



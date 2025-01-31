from django.test import TestCase
from rest_framework.test import APIClient
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        FAQ.objects.all().delete()

    def test_save_translations(self):
        # Create FAQ with correct question for Django
        faq = FAQ.objects.create(
            question="What is Django?",  # Use "What is Django?" as the question
            answer="Django is a web framework."
        )

        # Ensure the translations for Django are correct
        self.assertEqual(faq.question_hi, "Django क्या है?")
        self.assertEqual(faq.question_bn, "জ্যাঙ্গো কী?")

    def test_get_question_in_language(self):
        faq = FAQ.objects.create(
            question="What is Django?",  # Use "What is Django?" as the question
            answer="Django is a web framework."
        )

        # Test translations for Django
        self.assertEqual(faq.get_question_in_language('hi'), "Django क्या है?")
        self.assertEqual(faq.get_question_in_language('bn'), "জ্যাঙ্গো কী?")
        self.assertEqual(faq.get_question_in_language('en'), "What is Django?")

class FAQApiTest(TestCase):
    def setUp(self):
        FAQ.objects.all().delete()
        self.client = APIClient()

    def test_faq_list_in_english(self):
        FAQ.objects.create(
            question="What is Django?",  # Use "What is Django?" as the question
            answer="Django is a web framework."
        )

        # Test the API response for English (default)
        response = self.client.get('/api/faqs/?lang=en')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("What is Django?", data['faqs'][0]['question'])

    def test_faq_list_in_hindi(self):
        FAQ.objects.create(
            question="What is Django?",  # Use "What is Django?" as the question
            answer="Django is a web framework."
        )

        # Test the API response for Hindi
        response = self.client.get('/api/faqs/?lang=hi')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("Django क्या है?", data['faqs'][0]['question'])

    def test_faq_list_in_bengali(self):
        FAQ.objects.create(
            question="What is Django?",  # Use "What is Django?" as the question
            answer="Django is a web framework."
        )

        # Test the API response for Bengali
        response = self.client.get('/api/faqs/?lang=bn')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("জ্যাঙ্গো কী?", data['faqs'][0]['question'])

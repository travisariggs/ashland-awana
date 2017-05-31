import unittest

from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from .models import Student, Verse, Recitation


class StudentModelTests(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_student_birthday_required(self):
        s = Student(first_name="Johnny", last_name="Appleseed")
        with self.assertRaises(IntegrityError):
            s.save()


class VerseModelTests(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip("How to validate at the model layer?")
    def test_verse_awana_book_required(self):
        v = Verse(text="Jesus wept.", awana_verse=2)
        #  with self.assertRaises(IntegrityError):
        with self.assertRaises(ValidationError):
            v.save()

    def test_verse_awana_verse_required(self):
        v = Verse(text="Jesus wept.", awana_book='C-HON')
        with self.assertRaises(IntegrityError):
            v.save()


class RecitationModelTests(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_valid_student_required(self):
        v = Verse(text="Jesus wept.", awana_verse=1, awana_book='C-HON')
        v.save()
        r = Recitation(verse_id=v.id, result='S')
        with self.assertRaises(IntegrityError):
            r.save()

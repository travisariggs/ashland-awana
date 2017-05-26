from django.db import models

class Student(models.Model):
    """Model for Awana Students"""

    MALE = 'M'
    FEMALE= 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True
    )

    birthday = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{first} {last}".format(first=self.first_name,
                                       last=self.last_name)


class Verse(models.Model):
    """Model for Awana memory verses"""

    AWANA_BOOK_CHOICES = (
        ('HON', 'HONEYCOMB'),
        ('APP', 'APPLESEED')
    )

    text = models.TextField()
    bible_book = models.CharField(max_length=30, blank=True)
    bible_chapter = models.IntegerField(blank=True)
    bible_verse = models.IntegerField(blank=True)
    awana_book = models.CharField(max_length=5, choices=AWANA_BOOK_CHOICES)
    awana_verse = models.IntegerField()

    def __str__(self):
        return self.text


class Recitation(models.Model):
    """Model for a student's attempt to recite an Awana memory verse"""

    RESULT_CHOICES = (
        ('F', 'Failed'),
        ('H', 'Success with help'),
        ('S', 'Success'),
    )

    result = models.CharField(
        max_length=1,
        choices=RESULT_CHOICES,
        default='F',
    )

    student = models.ForeignKey(Student)
    verse = models.ForeignKey(Verse)
    recited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.result

    def was_successful(self):
        return self.result in ('H', 'S')

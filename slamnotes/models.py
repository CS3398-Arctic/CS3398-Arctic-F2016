"""slamnotes Models Configuration

Several class-based models. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/db/models/
"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator
from django.forms import ModelForm, Textarea


class School(models.Model):
    """School model"""
    name = models.CharField(max_length=100)
    website = models.CharField(validators=URLValidator)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    """Instructor model"""
    name_first = models.CharField(max_length=30)
    name_last = models.CharField(max_length=40)

    def __str__(self):
        return self.name_first + self.name_last


class Course(models.Model):
    """Course model"""
    school = models.ForeignKey(School)
    instructor = models.ForeignKey(Instructor)
    title = models.CharField(max_length=100)
    prefix = models.CharField()
    number = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(9999),
            MinValueValidator(0)
        ])
    postfix = models.CharField(max_length=1)

    def __str__(self):
        return self.title


class Section(models.Model):
    """Section model"""
    course = models.ForeignKey(Course)
    instructor = models.ForeignKey(Instructor)
    number = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(999),
            MinValueValidator(0)
        ])
    special = models.CharField(max_length=8)

    def __str__(self):
        if not self.special:
            return self.number
        return self.special


class Day(models.Model):
    """Class day model"""
    date = models.DateField()

    def __str__(self):
        return self.date


class Note(models.Model):
    """Note model"""
    body_text = models.TextField()
    author = models.ForeignKey(User)
    section = models.ForeignKey(Section)
    day = models.ForeignKey(Day)
    created_date = models.DateField()

    def __str__(self):
        return self.body_text


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['body_text']
        widgets = {
            'name': Textarea(attrs={'placeholder': 'Write a note...'}),
        }

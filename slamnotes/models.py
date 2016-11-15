"""slamnotes Models Configuration

Several class-based models. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/db/models/
"""
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.mail import send_mail
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator
from django.db import models
from django.forms import ModelForm, Textarea, PasswordInput, EmailInput, ValidationError
from django.utils import timezone


class UserManager(BaseUserManager):
    """
    A custom user manager class based on UserManager in django.contrib.auth.models
    implementing a user manager that requires an email and a password.
    """
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def natural_key(self):
        return self.email


def validate_txstate_email(value):
    """Checks that the email input during user creation is a @txstate.edu, returns error if not."""
    if '@txstate.edu' not in value:
        raise ValidationError('Must be a @txstate.edu address')


class User(AbstractBaseUser, PermissionsMixin):
    """
    A custom user class based on AbstractUser implementing a fully featured User model with
    admin-compliant permissions.

    Email and password are required. Other fields are optional.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': "A user with that email already exists.",
        },
        validators=[validate_txstate_email]
    )
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text='Designates whether this user should be treated as active. '
                  'Deselect this instead of deleting accounts.',
    )
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = False # Used to output emails in JSON instead of

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class School(models.Model):
    """School model"""
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100, validators=[URLValidator, ])

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
    school = models.ForeignKey(School, blank=True)
    instructor = models.ForeignKey(Instructor, blank=True)
    title = models.CharField(max_length=100)
    prefix = models.CharField(max_length=2)
    number = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(9999),
            MinValueValidator(0)
        ])
    postfix = models.CharField(max_length=1)

    def __str__(self):
        return self.title


class Channel(models.Model):
    """Channel model"""
    course = models.ForeignKey(Course, blank=True)
    instructor = models.ForeignKey(Instructor, blank=True)
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


class Session(models.Model):
    """Class session model"""
    date = models.DateField()

    def __str__(self):
        return self.date


class Note(models.Model):
    """Note model"""
    body_text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    channel = models.ForeignKey(Channel, null=True, blank=True)
    session = models.ForeignKey(Session, null=True, blank=True)
    created_date = models.DateTimeField('date created', default=timezone.now)
    modified_date = models.DateTimeField('date modified', default=timezone.now)

    def __str__(self):
        return self.body_text


class NoteForm(ModelForm):
    """Note model form"""
    class Meta:
        model = Note
        fields = ['body_text']
        labels = {
            'body_text': '',
        }
        widgets = {
            'body_text': Textarea(attrs={'placeholder': 'Write a note...', 'cols': '', 'rows': ''}),
        }


class SignupForm(ModelForm):
    """User model form"""
    class Meta:
        model = User
        fields = ['email', 'password']

        labels = {
            'email': '',
            'password': '',
        }
        widgets = {
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'password': PasswordInput(attrs={'placeholder': 'Password'}),
        }


class LoginForm(ModelForm):
    """Login model form"""
    class Meta:
        model = User
        fields = ['email', 'password']

        labels = {
            'email': '',
            'password': '',
        }
        widgets = {
            'email': EmailInput(attrs={'placeholder': 'Email'}),
            'password': PasswordInput(attrs={'placeholder': 'Password'}),
        }

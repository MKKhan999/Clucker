from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[RegexValidator(
            regex=r'^@\w{3,}$',
            message='Username must consist of @ followed by at least three alphanumericals'
        )]
    )
    first_name = models.CharField(
        max_length=50,
        blank=False
    )
    last_name = models.CharField(
        max_length=50,
        blank=False
    )
    email = models.EmailField(
        unique=True, blank=False
    )
    bio = models.CharField(max_length=520, blank=True)

    password = models.CharField(max_length=520, validators = [RegexValidator(regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$',
    message='Password must be an uppercase character, lowercase character and a number'      )])

    def __str__(self):
        return self.username



class Post(models.Model):
    text = models.CharField(max_length=280, blank=True)
    created_at = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    class Meta:

        ordering = ['-created_at']
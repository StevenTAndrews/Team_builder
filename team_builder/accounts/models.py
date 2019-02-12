from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.urls import reverse, reverse_lazy
from django.db import models
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Users must have an email address.")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=100, default='')
    bio = models.TextField(max_length=500, blank=True, default='')
    image = models.ImageField(upload_to="profile_image/", blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username


ANDROID = "Android"
DESIGN = "Design"
JAVA = "Java"
PHP = "PHP"
PYTHON = "Python"
RAILS = "Rails"
WORDPRESS = "Wordpress"
iOS = "iOS"
SKILLES_CHOICES = (
    (ANDROID, "Android"),
    (DESIGN, "Design"),
    (JAVA, "Java"),
    (PHP, "PHP"),
    (PYTHON, "Python"),
    (RAILS, "Rails"),
    (WORDPRESS, "Wordpress"),
    (iOS, "iOS")
)

class Skill(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, choices=SKILLES_CHOICES)
from django.conf import settings
from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    timeline = models.CharField(max_length=255)
    requirements = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    

class Position(models.Model):
    ANDROID = "Android"
    DESIGN = "Design"
    JAVA = "Java"
    PHP = "PHP"
    PYTHON = "Python"
    RAILS = "Rails"
    WORDPRESS = "Wordpress"
    iOS = "iOS"
    SKILLES_CHOICES = (
        (ANDROID, "Android Developer"),
        (DESIGN, "Designer"),
        (JAVA, "Java Developer"),
        (PHP, "PHP Developer"),
        (PYTHON, "Python Developer"),
        (RAILS, "Rails Developer"),
        (WORDPRESS, "Wordpress Developer"),
        (iOS, "iOS Developer")
    )

    project = models.ForeignKey(
        Project,
        null=True,
        related_name="positions",
        on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True)
    skill = models.CharField(
        max_length=20,
        choices=SKILLES_CHOICES,
        default="",
        blank=True)
    position_filled = models.BooleanField(default=False, blank=True)
    applicants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='Application')

    def __str__(self):
        return self.title


class Application(models.Model):
    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="application"
    )
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)

    def __str__(self):
        return "{}, {}".format(self.applicant, self.position)


class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notification"
    )
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    message = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user)
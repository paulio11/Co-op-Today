from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Task(models.Model):

    DAYS = (
        ("Sunday", "Sunday"),
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
    )

    TLS = (
        ('Paul', 'Paul'),
        ('Graham', 'Graham'),
        ('Stephen', 'Stephen'),
        ('Jordon', 'Jordon'),
    )

    # REPEAT = (
    #     ('weekly', 'Weekly'),
    #     ('every 2 weeks', 'Every 2 weeks'),
    #     ('every 3 weeks', 'Every 3 weeks')
    # )

    name = models.CharField(max_length=500)
    due = models.DateField(blank=True, null=True)
    day = models.CharField(max_length=10, choices=DAYS)
    assigned_to = models.CharField(max_length=20, choices=TLS, blank=True)
    description = models.TextField(max_length=500, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class OtherTasks(models.Model):

    TLS = (
        ('Paul', 'Paul'),
        ('Graham', 'Graham'),
        ('Stephen', 'Stephen'),
        ('Jordon', 'Jordon'),
    )

    name = models.CharField(max_length=500)
    due = models.DateField(blank=True, null=True)
    assigned_to = models.CharField(max_length=20, choices=TLS, blank=True)
    description = models.TextField(max_length=500, blank=True)
    done = models.BooleanField(default=False)
    photo = CloudinaryField('image', blank=True)

    def __str__(self):
        return f'{self.name}'


class Handover(models.Model):

    message = models.TextField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    photo = CloudinaryField('image', blank=True)
    photo2 = CloudinaryField('image', blank=True)
    photo3 = CloudinaryField('image', blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='handover')
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Handover for {self.date}'

    class Meta:
        ordering = ['date']


class Event(models.Model):

    title = models.CharField(max_length=500)
    date = models.DateField()
    description = models.TextField(max_length=1000, blank=True)
    time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date']

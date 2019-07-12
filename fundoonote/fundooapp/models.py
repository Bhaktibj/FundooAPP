from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Regex validators
validate_alphanumeric = RegexValidator(r'^[a-zA-Z0-9]*$', 'Only alphanumeric characters are allowed.')
validate_alphabetical = RegexValidator('^[a-zA-Z]', 'Only Alphabetical Characters are allowed.')

# this model is used for RestRegister
class  UserProfile(models.Model):
    user = models.CharField(max_length=30)

    def __str__(self):
        return self.user

"""Notes Model """
class Notes(models.Model):
    # title field  contains the validators
    title = models.CharField("Title",max_length=400, validators=[validate_alphanumeric])
    description = models.CharField("Description",max_length=100, validators=[validate_alphabetical])
    collaborator = models.ManyToManyField(User, related_name='notes')
    pub_date = models.DateTimeField(auto_now=True)
    remainder = models.DateTimeField(default=None, null=True, blank=True)
    is_archive = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    # color choice
    COLOR_CHOICES = (
        ('Red','Red'),
        ('Ged','Green'),
        ('Blue','Blue'),
    )
    color = models.CharField(default='Green', max_length=50, blank=True,choices=COLOR_CHOICES, null=True)
    image = models.ImageField(default=None, null=True)
    trash = models.BooleanField(default=False)

    # print string Format
    def __str__(self):
        return self.title

    objects = models.Manager()

""" Label Models"""
class Label(models.Model):
    text = models.CharField(max_length=100, validators=[validate_alphabetical])
    pub_date = models.DateTimeField(auto_now=True)
    created_By = models.ForeignKey(User, related_name='label_created_by', on_delete=models.CASCADE)
    note = models.ForeignKey(Notes, related_name='notes', on_delete=models.CASCADE, blank=True, null=True)

    # print string Format
    def __str__(self):
        return  self.text

""" AWS Models"""
class AWSModel(models.Model):
    bucket_name = models.CharField(max_length=100, unique=True)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.bucket_name


from __future__ import unicode_literals

from django.db import models
import re
emailREGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['input_first_name']) < 1:
            errors["first_name"] = "First name should be more than 1 characters"
        if len(postData['input_last_name']) < 1:
            errors["last_name"] = "last name should be more than 1 characters"
        if not emailREGEX.match(postData['input_email']):
            errors["email"] = "Email must be in proper format"
        return errors;

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {}>".format(self.first_name, self.last_name)

from django.db import models
import re

class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(post_data['first_name']) < 1:
            errors["first_name"] = "first name can not be empty"

        if len(post_data['last_name']) < 1:
            errors["last_name"] = "Last name can not be empty "

        if len(post_data['user_email']) < 1:
            errors["user_email"] = "email can not be empty "

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['user_email']):            
            errors['email'] = "Invalid frommat email address!"

        if (post_data['user_password'] != post_data['password_confirm'] ):
            errors["password_confirm"] = "password did not match"

        if len(post_data['user_password']) < 8:
            errors["user_password"] = "password must be 8 charicters log"
        return errors



# Create your models here.
class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    user_email= models.CharField(max_length=255)
    user_password= models.CharField(max_length=255)
    objects = UserManager()



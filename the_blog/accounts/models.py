from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


#creating custom user manager
class CustomerUserManager(BaseUserManager):
    def create_user(self,email, password, **extra_fields):
        email =self.normalize_email(email)

        user=self.model(
            email =email,
            **extra_fields
        )
        #seeting a password 
        user.set_password(password)

        user.save()

        return user
 



    #method for creating a superuser
    def create_superuser(self, email, password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")


        return self.create_user(email=email, password=password,**extra_fields)



class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=100)

    objects=CustomerUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


    def __str__(self):
        return self.username
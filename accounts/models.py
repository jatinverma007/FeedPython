# -*- coding: utf-8 -*-
import logging

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

from uuid import uuid4



class MyUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

from django.contrib.auth import get_user_model

User = get_user_model()
logger = logging.getLogger(__name__)

class BaseModel(models.Model):
    """
    All models extend from this model
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_by = models.ForeignKey(
        User,
        related_name='%(app_label)s_%(class)s_created_by',
        null=True, blank=True, on_delete=models.SET_NULL
    )
    last_modified_by = models.ForeignKey(
        User,
        related_name='%(app_label)s_%(class)s_last_modified_by',
        null=True, blank=True, on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True




class AppUser(BaseModel):
    """
    This class represents a User of the website, it inherits from AbstractUser
    """
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False, unique=True)
    email_verified = models.BooleanField(null=False, default=False)
    phone_number = models.CharField(max_length=15, blank=False)
    address = models.TextField(blank=False)
    bio = models.TextField(blank=True)
    friends = models.ManyToManyField("AppUser", related_name='user_friends', blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['created_at']



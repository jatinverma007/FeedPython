
from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import (
    AppUser
)

from .models import AppUser

User = get_user_model()

class UserSignUpSerializer(serializers.ModelSerializer):

    class Meta():
        model = AppUser
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'address'
        ]

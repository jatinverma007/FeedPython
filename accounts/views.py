# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import User
from django.http import request, response

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response

from .serializers import (
    UserSignUpSerializer
) 
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import redirect;
from rest_framework.views import APIView
from rest_framework import status
from copy import copy

User = get_user_model()

class UserSignupAPIView(APIView):
    serializer_class = UserSignUpSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        email = data.get('email')

        email_users = User.objects.filter(email=email)
        if email_users:
            return Response(
                get_response_dict(USER_EMAIL_ALREADY_EXIST),
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            try:
                serializer.save()
            except:
                response_data = serializer.data
                return Response(
                get_response_dict(BAD_REQUEST, response_data),
                status=status.HTTP_400_BAD_REQUEST
            )
            response_data = serializer.data
            return Response(
                get_response_dict(USER_CREATE_SUCCESS, response_data),
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                get_response_dict(INVALID_POST_DATA),
                status=status.HTTP_400_BAD_REQUEST
            )
            

STATUS_CODE = "code"
MESSAGE = "msg"
DATA = 'data'

INVALID_POST_DATA = "7700"
USER_EMAIL_ALREADY_EXIST = "9003"
USER_CREATE_SUCCESS = "2999"
BAD_REQUEST = "0000"


RESPONSE_LOOKUP = {
BAD_REQUEST: {
    STATUS_CODE: int(BAD_REQUEST),
    MESSAGE: "Bad request provided"
},
INVALID_POST_DATA: {
    STATUS_CODE: int(INVALID_POST_DATA),
    MESSAGE: "Invalid or no data provided."
},

USER_EMAIL_ALREADY_EXIST: {
    STATUS_CODE: int(USER_EMAIL_ALREADY_EXIST),
    MESSAGE: "User with given email already exists"
},
USER_CREATE_SUCCESS: {
    STATUS_CODE: int(USER_CREATE_SUCCESS),
    MESSAGE: "User created successfully"
},
}

def get_response_dict(lookup, data=None, substitute=None):
    response_data = copy(RESPONSE_LOOKUP.get(lookup, {
        STATUS_CODE: 0,
        MESSAGE: "Something Went Wrong",
        DATA: ''
    }))
    if data is not None:
        response_data[DATA] = data
    if substitute:
        response_data[MESSAGE] = response_data[MESSAGE] % substitute
    return response_data


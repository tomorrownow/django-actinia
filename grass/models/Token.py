###############################################################################
# Filename: Token.py                                                           #
# Project: OpenPlains Inc.                                                     #
# File Created: Tuesday June 7th 2022                                          #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Mon Mar 18 2024                                               #
# Modified By: Corey White                                                     #
# -----                                                                        #
# License: GPLv3                                                               #
#                                                                              #
# Copyright (c) 2023 OpenPlains Inc.                                                #
#                                                                              #
# django-actinia is an open-source django app that allows for with             #
# the Actinia REST API for GRASS GIS for distributed computational tasks.      #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU General Public License as published by         #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU General Public License for more details.                                 #
#                                                                              #
# You should have received a copy of the GNU General Public License            #
# along with this program.  If not, see <https://www.gnu.org/licenses/>.       #
#                                                                              #
###############################################################################

from django.db import models
from django.utils import timezone
from django.conf import settings
from .abstracts.ObjectAuditAbstract import ObjectAuditAbstract
from grass.models.enums import TokenTypeEnum
from enum import Enum, unique
import requests
import json


@unique
class USER_TASK(Enum):
    TOKEN = "token"
    API_KEY = "api_key"


class Token(ObjectAuditAbstract):
    """
    This module contains the Token model, which represents a user token generated by actinia.

    The Token model has the following fields:
    - token: a string representing the token
    - user: a foreign key to the auth.User model
    - actinia_user: a foreign key to the ActiniaUser model
    - expires: a datetime representing the expiration date of the token
    - token_type: a Enum (TokenTypeEnum) representing the type of token (e.g. USER, TASK)
    - api_key: a boolean value indicating if the token is an api_key (does not expire)

    The Token model also has the following methods:
    - is_expired(): returns True if the token is expired
    - is_active(): returns True if the token is active (i.e. not expired)
    """

    token = models.CharField(max_length=255, blank=False, unique=True, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tokens"
    )
    actinia_user = models.ForeignKey(
        "grass.ActiniaUser",
        on_delete=models.CASCADE,
        null=True,
        related_name="actinia_tokens",
    )
    expires = models.DateTimeField(null=True)
    token_type = models.CharField(
        max_length=2, choices=TokenTypeEnum.choices, default=TokenTypeEnum.USER
    )
    api_key = models.BooleanField(default=False)

    def __actinia_token_request_url(self, base_url, task):
        """
        Provides the url to an Actinia token and api.
        """
        base_url = f"{base_url}/{task}"

        return base_url

    def is_expired(self):
        """Returns true if the token is expired"""
        now = timezone.now()
        return now > self.expires

    def is_active(self):
        """Returns true if the token is expired"""
        now = timezone.now()
        return now < self.expires

    @classmethod
    def generate_actinia_token(
        cls, base_url, actinia_user, api_key=False, expiration_time=86400
    ):
        """
        Generate authorization token for user and store in Tokens
        """
        query = {}

        if api_key:
            expiration_time = None
        if expiration_time:
            is_integer = isinstance(expiration_time, int)
            if is_integer:
                query = {"expiration_time": expiration_time}
            else:
                print("Expiration time must be an integer")
                raise

        task = USER_TASK.API_KEY if api_key else USER_TASK.TOKEN

        url = cls.__actinia_token_request_url(base_url, task)
        auth = actinia_user._auth()
        try:
            response = requests.get(url, auth=auth, params=query)
            if response.status_code != 200:
                raise Exception(f"Failed to create {task}: {response.status_code}")

            token = response.text
            user = actinia_user.user
            new_token = cls(
                token=token,
                token_type=TokenTypeEnum.ACTINIA,
                api_key=api_key,
                expires=expiration_time,
                actinia_user=actinia_user,
                user=user,
            )
            new_token.save()

        except Exception as e:
            print(e)
            raise

###############################################################################
# Filename: Token.py                                                           #
# Project: OpenPlains                                                          #
# File Created: Tuesday June 7th 2022                                          #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Tue Jun 07 2022                                               #
# Modified By: Corey White                                                     #
# -----                                                                        #
# License: GPLv3                                                               #
#                                                                              #
# Copyright (c) 2022 OpenPlains                                                #
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
from django.contrib.auth.models import User
from django.utils import timezone
from tomlkit import datetime
from actinia.models.ActiniaUser import ActiniaUser
from actinia.models.ObjectAuditAbstract import ObjectAuditAbstract
from actinia.models.enums import TokenTypeEnum


class Token(ObjectAuditAbstract):
    """
    User token generated by actinia.
    """

    token = models.CharField(max_length=255, blank=False, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    actinia_user = models.ForeignKey(ActiniaUser, on_delete=models.CASCADE)
    expires = models.DateTimeField()
    token_type = models.CharField(
        max_length=2, choices=TokenTypeEnum.choices, default=TokenTypeEnum.USER
    )

    def is_expired(self):
        """Returns true if the token is expired"""
        now = timezone.now()
        return now > self.expires

    def is_active(self):
        """Returns true if the token is expired"""
        now = timezone.now()
        return now < self.expires

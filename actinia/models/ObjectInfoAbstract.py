###############################################################################
# Filename: ObjectInfoAbstract.py                                              #
# Project: django-actinia                                                          #
# File Created: Tuesday June 7th 2022                                          #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Tue Jun 07 2022                                               #
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
from django.contrib.auth.models import User
from actinia.models.ObjectAuditAbstract import ObjectAuditAbstract
from actinia.models.Organization import Organization


class ObjectInfoAbstract(ObjectAuditAbstract):
    """
    Abstract class to add basic details to a database object
    """

    name = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=250, blank=True)
    owner = models.ForeignKey(User, editable=True, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)
    organization = models.ForeignKey(
        Organization, editable=True, on_delete=models.CASCADE
    )

    class Meta:
        abstract = True

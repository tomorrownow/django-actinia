###############################################################################
# Filename: Organization.py                                                    #
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
from actinia.models.ObjectAuditAbstract import ObjectAuditAbstract


class Organization(ObjectAuditAbstract):
    """
    Custom user class to manage actinia user.

    Attributes
    ----------
    id : int
        The default object id
    organization_id : str
        Unique hash identifier for the organization.
    organization_name : str
        The name of the organization.
    owner : int
        The user who is the owner of the organization.
    """

    organization_id = models.BigAutoField(primary_key=True)
    organization_name = models.CharField(max_length=50, blank=False, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # members =
    # teams =

    class Meta:
        contraints = [
            models.UniqueConstraint(
                fields=["organization_id"], name="unique_organization_id"
            )
        ]

    def members(self):
        """
        Generate a password for managed actinia user.
        """
        pass

    def teams(self):
        """
        Get a list of user's teams
        """
        pass

    def generateActiniaToken(self):
        """
        Generate authorization token for user and store in Tokens
        """
        pass

    def refreshActiniaToken(self):
        """
        Refresh users authentication token
        """
        pass

    def locations(self):
        """
        Get a list of user's locations
        """
        pass

    def projects(self):
        """
        Get a list of user's projects
        """
        pass

    def grass_templates(self):
        """
        Get list of user's GRASS Templates
        """
        pass

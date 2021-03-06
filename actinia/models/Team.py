###############################################################################
# Filename: Team.py                                                            #
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


from actinia.models.ObjectInfoAbstract import ObjectInfoAbstract

from django.db import models

from actinia.models.ActiniaUser import ActiniaUser


class Team(ObjectInfoAbstract):
    """
    Class representing a team

    Attributes
    ----------
    id : BigAutoField
        Auto generated Primary key of response
    name : str
        The name of the GRASS location
    description : str
        A description of the team.
    owner : str
        The user who owns the team
    members: str
        The members of the team
    """

    members = models.ManyToManyField(ActiniaUser, editable=True)

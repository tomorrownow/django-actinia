###############################################################################
# Filename: ActiniaSimpleResponseSerializer.py                                 #
# Project: OpenPlains Inc.                                                     #
# File Created: Tuesday June 7th 2022                                          #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Wed Apr 10 2024                                               #
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

from rest_framework import serializers
from .fields import ResponseStatusChoiceField, ResourceStatusChoiceField


class ActiniaSimpleResponseSerializer(serializers.Serializer):
    """
    Serializer to consume response from Actinia SimpleResponseResponseModel.

    Version
    -------
    Actinia 4.0

    Attributes
    ----------
    message : str
        A response message from acitina.
    status : str
        The status response from actinia
    """

    message = serializers.CharField(required=False, allow_blank=True, max_length=250)


class ResourceStatusSerializer(ActiniaSimpleResponseSerializer):
    """Serializer to consume response from Actinia API resource stutas"""

    status = ResourceStatusChoiceField()


class ResponseStatusSerializer(ActiniaSimpleResponseSerializer):
    """Serializer to consume response from Actinia API response stutas"""

    status = ResponseStatusChoiceField()

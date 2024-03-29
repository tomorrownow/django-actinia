###############################################################################
# Filename: test_GrassModuleSerializer.py                                      #
# Project: OpenPlains Inc.                                                     #
# File Created: Sunday December 17th 2023                                      #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Fri Mar 22 2024                                               #
# Modified By: Corey White                                                     #
# -----                                                                        #
# License: GPLv3                                                               #
#                                                                              #
# Copyright (c) 2023 OpenPlains Inc.                                           #
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


from grass.serializers import GrassModuleSerializer
from django.test import TestCase


class GrassModuleSerializerTest(TestCase):
    def test_valid_data(self):
        data = {
            "id": "module_id",
            "module": "r.univar",
            "inputs": [
                {"param": "param1", "value": "value1"},
                {"param": "param2", "value": "value2"},
            ],
            "outputs": [
                {"param": "param1", "value": "value1"},
                {"param": "param2", "value": "value2"},
            ],
            "flags": "-f",
            "stdin": "previous_module::stdout",
            "stdout": {"id": "1", "format": "json", "delimiter": ","},
            "overwrite": True,
            "verbose": False,
            "superquiet": True,
            "interface_description": False,
        }

        serializer = GrassModuleSerializer(data=data)
        if serializer.is_valid():
            assert serializer.validated_data == data
        else:
            print(serializer.errors)

    def test_invalid_data(self):
        data = {
            "id": None,
            "module": None,
            "inputs": [
                {"name": "input_param1", "value": "value1"},
                {"name": "input_param2", "value": "value2"},
            ],
            "outputs": [
                {"name": "output_param1", "value": "value3"},
                {"name": "output_param2", "value": "value4"},
            ],
            "flags": "-f",
            "stdin": "previous_module::stdout",
            "stdout": {"parser": "json", "options": {"key": "value"}},
            "overwrite": True,
            "verbose": False,
            "superquiet": True,
            "interface_description": False,
        }

        serializer = GrassModuleSerializer(data=data)
        assert not serializer.is_valid()

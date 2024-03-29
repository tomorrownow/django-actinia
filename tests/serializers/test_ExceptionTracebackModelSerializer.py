from django.test import TestCase

###############################################################################
# Filename: test_ExceptionTracebackModelSerializer.py                          #
# Project: OpenPlains Inc.                                                     #
# File Created: Sunday December 17th 2023                                      #
# Author: Corey White (smortopahri@gmail.com)                                  #
# Maintainer: Corey White                                                      #
# -----                                                                        #
# Last Modified: Wed Mar 06 2024                                               #
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


from grass.serializers.ExceptionTracebackModelSerializer import (
    ExceptionTracebackModelSerializer,
)


class ExceptionTracebackModelSerializerTestCase(TestCase):
    def test_serializer_fields(self):
        serializer = ExceptionTracebackModelSerializer()
        fields = serializer.fields

        assert "message" in fields
        assert "type" in fields
        assert "traceback" in fields

    def test_serializer_valid_data(self):
        data = {
            "message": "Test message",
            "type": "Test type",
            "traceback": ["Line 1", "Line 2", "Line 3"],
        }
        serializer = ExceptionTracebackModelSerializer(data=data)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data, data)

    def test_serializer_invalid_data(self):
        data = {
            "message": "Test message",
            "type": "Test type",
            "traceback": "Invalid traceback",  # Should be a list
        }
        serializer = ExceptionTracebackModelSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("traceback", serializer.errors)

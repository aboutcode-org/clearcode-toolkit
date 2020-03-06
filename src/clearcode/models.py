# -*- coding: utf-8 -*-
#
# Copyright (c) nexB Inc. and others. All rights reserved.
#
# ClearCode is a free software tool from nexB Inc. and others.
# Visit https://github.com/nexB/clearcode-toolkit/ for support and download.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models


class CDitem(models.Model):
    """
    A simple key/value pair model where the key is the path to a JSON file as
    stored in ClearlyDefined blob storage and the value is a GZipped compressed
    JSON file content, stored as a binary bytes blob.
    """
    path = models.CharField(primary_key=True, max_length=2048,
        help_text='Path to the original file in the ClearlyDefined file storage.'
    )

    content = models.BinaryField(
        help_text='Actual gzipped JSON content.'
    )

    last_modified = models.DateTimeField(
        help_text='Date that this record was last modified.',
        db_index=True,
    )

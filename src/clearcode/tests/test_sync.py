#
# Copyright (c) 2020 by nexB, Inc. http://www.nexb.com/ - All rights reserved.
#
import gzip
import json

from django.test import TestCase
from django.utils import timezone

from clearcode.models import CDitem
from clearcode.sync import db_saver


class SyncDbsaverTestCase(TestCase):
    def setUp(self):
        self.test_path = 'composer/packagist/yoast/wordpress-seo/revision/9.5-RC3.json'
        self.test_content = {'test': 'content'}

        self.cditem0 = CDitem.objects.create(
            path=self.test_path, 
            content=gzip.compress(json.dumps(self.test_content).encode('utf-8')),
        )

    def test_db_saver_idential_path(self):
        db_saver(content=self.test_content, blob_path=self.test_path)
        self.assertEqual(1, len(CDitem.objects.all()))

    def test_db_saver_different_path(self):
        db_saver(content=self.test_content, blob_path='new/blob/path.json')
        self.assertEqual(2, len(CDitem.objects.all()))

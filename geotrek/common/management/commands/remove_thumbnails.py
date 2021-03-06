# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.core.management.base import BaseCommand
from django.conf import settings

from easy_thumbnails.models import Thumbnail


class Command(BaseCommand):
    help = "Remove all thumbnails"

    def handle(self, *args, **options):
        thumbnails = Thumbnail.objects.all()

        for thumbnail in thumbnails:
            path = os.path.join(settings.MEDIA_ROOT, thumbnail.name)
            if os.path.exists(path):
                os.remove(path)
            thumbnail.delete()
            if options['verbosity'] > 0:
                self.stdout.write("{pict} deleted".format(pict=thumbnail.name))

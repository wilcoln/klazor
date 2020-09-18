# Copyright (c) 2020 Quidely
#
# All Rights Reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.
# This file is proprietary and confidential.

""" Command use for seeding initial data in the quidely_eat app."""
import decimal
import random

from django.core import management
from django.core.management import base
from rest_framework.authtoken.models import Token

from klazor import models, settings
from seed import factories


class Command(base.BaseCommand):
    help = "Seed Klazor with sample data."

    def handle(self, *args, **options):

        # Super user infos
        username = 'klazor'
        email = ''
        password = username

        self.output('Flushing the database ...')

        # Flush the database
        management.call_command('flush', interactive=False)

        models.User.objects.create_superuser(username, email, password)

        self.output('Seeding initial data ...')

        # Create Root folder
        factories.FolderFactory(name='root')

        

    def output(self, msg):
        self.stdout.write(msg)

    def output_user_data(self, username, email, password, token):
        # Output user data
        self.output('Username: ' + username)
        self.output('Email: ' + email)
        self.output('Password: ' + password)
        self.output('Token: ' + token.key)

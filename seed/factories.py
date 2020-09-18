# Copyright (c) 2020 Quidely
#
# All Rights Reserved.
# This file is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.

"""Factories for Django models for the Klazor project."""

# Classes defined in this module do not need a docstring
# as we know up front that they're fa for their corresponding model.
# pylint: disable=missing-class-docstring

import factory
import pytz
from factory.faker import faker

from klazor import models

fake = faker.Faker()


#####################
# General
####################
class UserFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.User

    username = factory.Sequence(lambda n: 'username%d' % n)
    email = factory.Faker('email')
    phone = factory.Faker('phone_number')


class FolderFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Folder

    name = factory.Faker('name')
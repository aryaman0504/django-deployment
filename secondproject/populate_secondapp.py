import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','secondproject.settings')

import django
# Import settings
django.setup()

import random
from secondapp.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        first = fakegen.first_name()
        last = fakegen.last_name()
        mail = fakegen.email()

        t = User.objects.get_or_create(first_name=first,last_name=last,Email=mail)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')

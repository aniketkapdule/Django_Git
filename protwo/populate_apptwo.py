import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'protwo.settings')

import django
django.setup()

from apptwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first = fake_name[0]
        fake_last = fake_name[1]
        fake_email = fakegen.email()

        #New entry
        user = User.objects.get_or_create(first_name = fake_first, last_name = fake_last, email=fake_email)[0]


if __name__ == '__main__':
    print('Populatinig')
    populate(20)
    print("Complete")

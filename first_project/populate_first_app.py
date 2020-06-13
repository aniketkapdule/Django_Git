import os

# to configuring settings for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

#FAKE POP SCRIPT
import random
from first_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    #following command returns tuple and we just need the first object
    #in that tuple that's why there is [0] in the end
    '''
    Returns a tuple of (object, created), where object is the retrieved or 
    created object and created is a boolean specifying whether a new object 
    was created.
    '''
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):

    for entry in range(N):
        #creating the topic
        top = add_topic()

        #generating some fake entries
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #putting it into webpage
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #utting the webpg into access records
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete!')
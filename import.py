import csv, sys, os

project_dir = os.getcwd() + '/djangopractice'
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django
django.setup()
from adoptions.models import Pet, Vaccine
data = csv.reader(open(os.getcwd() + "/pets.csv"), delimiter=",")

from datetime import datetime

VACCINES_NAMES = [
    'Canine Parvovirus',
    'Canine Distemper',
    'Canine Rabies',
    'Feline Herpes Virus 1',
    'Feline Rabies'
]

for vaccine_name in VACCINES_NAMES:
    vacs = Vaccine.objects.filter(name=vaccine_name)
    if (len(vacs) == 0):
        vac = Vaccine(name=vaccine_name)
        vac.save()

for row in data:
    if row[0] != 'create_date':
        pet = Pet()
        pet.name = row[0]
        pet.species = row[1]
        pet.breed = row[2]
        pet.sex = row[3]
        pet.age = int(row[4])
        pet.submitter = row[5]
        pet.submission_date = datetime.strptime(row[6], '%m/%d/%Y')
        pet.description = row[7]
        pet.picture = row[9]
        pet.save()

        # Many-to-Many relation
        raw_vaccinations_names = row[8]
        vaccinations = raw_vaccinations_names.split(' | ')
        for vaccine in vaccinations:
            vaccine_obj = Vaccine.objects.get(name=vaccine)
            pet.vaccinations.add(vaccine_obj)
        pet.save()

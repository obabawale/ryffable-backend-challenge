from noun.models import *
import csv


def run():
    with open('noun/noun_data.csv') as file:
        reader = csv.reader(file)
        next(reader)
        
        Noun.objects.all().delete()

        for row in reader:
            print(row)

            place, _ = Place.objects.get_or_create(name=row[1])
            animal, _ = Animal.objects.get_or_create(name=row[2])
            food, _ = Food.objects.get_or_create(name=row[3])

            things = row[4].split("-")

            noun = Noun(
                name=row[0],
                place=place,
                animal=animal,
                food=food
            )
            noun.save()
            for thing in things:
                noun.things.create(name=thing)
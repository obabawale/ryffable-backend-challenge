from noun.models import Noun
import csv


def run():
    with open('noun/noun_data.csv') as file:
        reader = csv.reader(file)
        next(reader)
        
        Noun.objects.all().delete()

        for row in reader:
            print(row)

            noun = Noun(
                name=row[0],
                place=row[1],
                animal=row[2],
                food=row[3],
                things=row[4],
            )
            noun.save()
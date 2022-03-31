from noun.models import Noun
import csv


def run():
    with open('noun/noun_data.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Noun.objects.all().delete()

        for row in reader:
            print(row)

            noun = Noun(
                title=row[0],
                title=row[1],
                title=row[2],
                title=row[3],
                title=row[4],
            )
            noun.save()
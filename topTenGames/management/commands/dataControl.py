
### file to import the CSV file videoGameSales.csv aquired from Kaggle
import csv
from django.core.management import BaseCommand

from topTenGames.models import Game

ALREDY_LOADED_ERROR_MESSAGE = '''there is already a full database in use, delete 
your current database and restart'''

class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from children.csv"

    def handle(self, *args, **options):
    
        # Show this if the data already exist in the database
        if Game.objects.exists():
            print('child data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
            
        # Show this before loading the data into the database
        print("Importing daya into the SQLite database... this may take a while...")
        fields = []
        games = []
        # Create your models here.
        
        with open('videoGameSales.csv', 'r') as csv_file:
            csvreader = csv.reader(csv_file)
            fields = next(csvreader)
            del fields[-1]
            del fields[0]
            for row in csvreader:
                workingDict = {}
                ##Name
                workingDict['name'] = row[1]
                ##Platform
                workingDict['platform'] = row[2]
                ##year
                if (row[3] == ""):
                    workingDict["year"] = 0
                else:
                    workingDict['year'] = row[3]
                ##genre
                workingDict['genre'] = row[4]
                ##publisher
                workingDict['publisher'] = row[5]
                ##na
                workingDict['na_sales'] = row[6]
                ##eu
                workingDict['eu_sales'] = row[7]
                ##jp
                workingDict['jp_sales'] = row[8]
                ##other
                workingDict['other_sales'] = row[9]
                ##global
                workingDict['global_sales'] = row[10]
                ##append to total list
                games.append(workingDict)
            ##Takes every game in the csv file and places it into the database
            for i in games:
                g = Game(name=i["name"], platform=i["platform"], year=i["year"], genre=i["genre"],
                publisher=i["publisher"], euSales=i["eu_sales"], jpSales=i["jp_sales"], naSales=i["na_sales"],
                otherSales=i["other_sales"], globalSales=i["global_sales"])
                g.save()



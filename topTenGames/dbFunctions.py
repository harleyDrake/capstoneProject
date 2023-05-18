from .models import Game

##List of game platforms
consoleRef = {
        "Atari 2600": "2600",
        "Nintendo": "NES",
        "Super Nintendo": "SNES",
        "Nintendo 64": "N64",
        "Game Cube": "GC",
        "Gameboy": "GB",
        "Gameboy Advance": "GBA",
        "Playstation": "PS",
        "Playstation 2": "PS2",
        "Playstation 3": "PS3",
        "Playstation 4": "PS4",
        "Xbox": "XB",
        "Xbox 360": "X360",
        "Xbox One": "XOne",
        "Wii": "Wii",
        "Nintendo DS": "DS",
        "Nintendo 3DS": "3DS",
        "PC" : "PC",
        "Sega Genesis" : "GEN",
        "Wii U": "WiiU",
        "PSP":"PSP",
        "PS Vita": "PSV",
                  }

def getGamesData(type, query):
    if(type == "decade"):
        if (query == "1980s"):
            ##the decade list is every thing from the 80s
            decadeList = Game.objects.filter(year__startswith="198").order_by("-globalSales")[:40]
        elif(query == "1990s"):
            decadeList = Game.objects.filter(year__startswith="199").order_by("-globalSales")[:40]
        elif(query == "2000s"):
            decadeList = Game.objects.filter(year__startswith="200").order_by("-globalSales")[:40]
        elif(query == "2010s"):
            decadeList = Game.objects.filter(year__startswith="201").order_by("-globalSales")[:40]
        ##Prepare the list of games by decade
        count = 1
        games = []
        for item in decadeList:
            game = {}
            game["name"] = item.name
            game["globalSales"] = int(item.globalSales*1000000)
            game["platform"] = item.platform
            game["genre"] = item.genre
            game["year"] = item.year
            game["id"] = count
            games.append(game)
            count += 1
        
        return games
    elif(type =="console"):
        decadeList = Game.objects.filter(platform=query).order_by("-globalSales")[:40]
        ##Prepare the list of games by console
        count = 1
        games = []
        for item in decadeList:
            game = {}
            game["name"] = item.name
            game["globalSales"] = int(item.globalSales*1000000)
            game["platform"] = item.platform
            game["genre"] = item.genre
            game["year"] = item.year
            game["id"] = count
            games.append(game)
            count += 1
        return games
    elif(type == "year"):
        yearList = Game.objects.filter(year=query).order_by("-globalSales")[:40]
        ##Prepare the list of games by console
        count = 1
        games = []
        for item in yearList:
            game = {}
            game["name"] = item.name
            game["globalSales"] = int(item.globalSales*1000000)
            game["platform"] = item.platform
            game["genre"] = item.genre
            game["year"] = item.year
            game["id"] = count
            games.append(game)
            count += 1
        return games
    
def getSalesData():
    gameSales = Game.objects.all()
    yearSales = {}
    yearList = []
    for i in range(1980, 2011):
        yearSales[i] = {
            "na_sales": 0,
            "eu_sales": 0,
            "jp_sales": 0,
            "other_sales": 0,
            "global_sales": 0
        }
        yearList.append(i)
    
    for game in gameSales:
        if(game.year not in yearList):
            continue
        else:
            year = game.year
            naSales = game.naSales*1000000
            euSales = game.euSales*1000000
            jpSales = game.jpSales*1000000
            otherSales = game.otherSales*1000000
            globalSales = game.globalSales*1000000
            ### increases the count of sales for a given year
            yearData = yearSales[year]
            yearData["na_sales"] += naSales
            yearData["eu_sales"] += euSales
            yearData["jp_sales"] += jpSales
            yearData["other_sales"] += otherSales
            yearData["global_sales"] += globalSales
    return yearSales

def prepareData(inputDict):
    years = []
    naSales = []
    euSales = []
    jpSales = []
    otherSales = []
    globalSales = []
    for year in range(1980, 2011):
        years.append(year)
        naSales.append(inputDict[year]["na_sales"])
        euSales.append(inputDict[year]["eu_sales"])
        jpSales.append(inputDict[year]["jp_sales"])
        otherSales.append(inputDict[year]["other_sales"])
        globalSales.append(inputDict[year]["global_sales"])
    return years, naSales, euSales, jpSales, otherSales, globalSales


from django.shortcuts import render
from .models import Game
import topTenGames.dbFunctions as dbf
import plotly.express as px


def index(request):
    context={}
    dbf.getSalesData()
    return render(request, "topTenGames/index.html", context)


###the big top 40 games
def top40(request):
    workingList = Game.objects.all().order_by("-globalSales")[:100]
    games = []
    count = 1
    ###prepare the list of items to be passed to the top 40 page
    for item in workingList:
        game = {}
        game["name"] = item.name
        game["globalSales"] = int(item.globalSales)*1000000
        game["platform"] = item.platform
        game["genre"] = item.genre
        game["year"] = item.year
        game["id"] = count
        games.append(game)
        count += 1

    ###Plotly chart
    xData = [i["name"] + " (" + i["platform"] + ")" for i in games[:40]]
    yData = [i["globalSales"] for i in games[:40]]
    fig = px.bar(y = xData, x = yData, title="The REAL Top 40",
                 labels={"y": "Games", "x": "Units sold"},
                 orientation='h', height=800)
    chart = fig.to_html()
    context = {"games": games, "chart": chart}
    return render(request, "topTenGames/top40.html", context)

##Sorting games by decade
def decade(request):
    context = {}
    if request.method == "POST":
        if(request.POST["decade"] == "1980s"):
            context["games"] = dbf.getGamesData("decade", "1980s")
        elif(request.POST["decade"] == "1990s"):
            context["games"] = dbf.getGamesData("decade", "1990s")
        elif(request.POST["decade"] == "2000s"):
            context["games"] = dbf.getGamesData("decade", "2000s")
        elif(request.POST["decade"] == "2010s"):
            context["games"] = dbf.getGamesData("decade", "2010s")
        ###Plotly chart
        xData = [i["name"] + " (" + i["platform"] + ")" for i in context["games"][:10]]
        yData = [i["globalSales"] for i in context["games"][:10]]
        fig = px.bar(y = xData, x = yData, title="Top Ten Games from the " + request.POST["decade"],
                 labels={"y": "Games", "x": "Units sold"},
                 orientation='h')
        chart = fig.to_html()
        context["chart"] = chart
        context["decade"] = request.POST["decade"];
    return render(request, "topTenGames/decade.html", context)

def consoles(request):
    context = {}
    if (request.method == "POST"):
        context["games"] = dbf.getGamesData("console", dbf.consoleRef[request.POST["console"]])
        ###Plotly chart
        xData = [i["name"] + " (" + i["platform"] + ")" for i in context["games"][:10]]
        yData = [i["globalSales"] for i in context["games"][:10]]
        fig = px.bar(y = xData, x = yData, title="Top Ten Games on the " + request.POST["console"],
                 labels={"y": "Games", "x": "Units sold"},
                 orientation='h')
        chart = fig.to_html()
        context["chart"] = chart
        context["console"] = request.POST["console"]
    return render(request, "topTenGames/consoles.html", context)

def year(request):
    context={}
    if(request.method == "POST"):
        yearInput = request.POST['year']
        try:
            yearInput = int(yearInput)
        ###Raise error for invalid error
        except:
            context["yearError"] = "Invalid Input, the value must be a year between 1980 and 2016."
        else:
            if(1980 <= yearInput <= 2016):
                context["games"] = dbf.getGamesData("year", yearInput)     
                context["year"] = str(yearInput)
                ###Plotly chart
                xData = [i["name"] + " (" + i["platform"] + ")" for i in context["games"][:10]]
                yData = [i["globalSales"] for i in context["games"][:10]]
                fig = px.bar(y = xData, x = yData, title="Top Ten Games from " + request.POST["year"],
                        labels={"y": "Games", "x": "Units sold"},
                        orientation='h')
                chart = fig.to_html()
                context["chart"] = chart
            else:
                context["yearError"] = "Year out of range, must be between 1980 and 2016"   
    return render(request, "topTenGames/year.html", context)

def sources(request):
    context = {}
    return render(request, "topTenGames/sources.html", context)

def totalSales(request):
    yearSales = dbf.getSalesData()
    years, naSales, euSales, jpSales, otherSales, globalSales = dbf.prepareData(yearSales)
    context = {}
    globalFig = px.scatter(y = globalSales, x = years, title="Global Video Game Sales between 1980 and 2010",
                 labels={"y": "Units Sold", "x": "Year"})
    globalChart = globalFig.to_html()
    context["globalSales"] = globalChart
    naFig = px.scatter(y = naSales, x = years, title="Video Game Sales between 1980 and 2010 in North America",
                 labels={"y": "Units Sold", "x": "Year"})
    naChart = naFig.to_html()
    context["naSales"] = naChart
    euFig = px.scatter(y = euSales, x = years, title="Video Game Sales between 1980 and 2010 in Europe",
                 labels={"y": "Units Sold", "x": "Year"})
    euChart = euFig.to_html()
    context["euSales"] = euChart
    jpFig = px.scatter(y = jpSales, x = years, title="Video Game Sales between 1980 and 2010 in Japan",
                 labels={"y": "Units Sold", "x": "Year"})
    jpChart = jpFig.to_html()
    context["jpSales"] = jpChart
    otherFig = px.scatter(y = otherSales, x = years, title="Video Game Sales between 1980 and 2010 in Other Regions",
                 labels={"y": "Units Sold", "x": "Year"})
    otherChart = otherFig.to_html()
    context["otherSales"] = otherChart

    return render(request, "topTenGames/salesData.html", context)
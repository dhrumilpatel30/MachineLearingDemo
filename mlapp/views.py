from django.shortcuts import render
from mlapp.forms import *
from mlapp.mlconfigration import *

# Create your views here.


def HomeView(request):
    form = DataForm()
    return render(request, "home.html", {"form": form})


def CalculateView(request):
    print(request.POST)
    form_data = request.POST
    mydict = {
        "day": int(form_data["date_day"]),
        "mnth": int(form_data["date_month"]),
        "year": int(form_data["date_year"]),
        "season": int(form_data["season"]),
        "holiday": int(form_data["holiday"]),
        "weekday": int(form_data["weekday"]),
        "workingday": int(form_data["workingday"]),
        "weathersit": int(form_data["weathersit"]),
        "temp": float(form_data["temp"]) * 0.01,
        "atemp": float(form_data["atemp"]) * 0.01,
        "hum": float(form_data["hum"]) * 0.01,
        "windspeed": float(form_data["windspeed"]) * 0.01,
    }
    result = Calculate(mydict)
    print(type(result))
    result1 = bytes.decode(result)
    print(type(result1))
    return render(request, "show.html", {"result": result1[13:25]})

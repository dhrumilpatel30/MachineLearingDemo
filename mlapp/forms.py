from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

MYBOOLEAN = [("1", "Yes"), ("0", "No")]
SEASONS = [
    ("1", "Spring"),
    ("2", "Summer"),
    ("3", "Autumn"),
    ("4", "Winter"),
]

DAYS = [
    ("0", "Sunday"),
    ("1", "Monday"),
    ("2", "Tuesday"),
    ("3", "Wednesday"),
    ("4", "Thursday"),
    ("5", "Friday"),
    ("6", "Saturday"),
]

SITUATION = [
    ("1", "Clear"),
    ("2", "Cloudy"),
    ("3", "Heavy Rain"),
]


class DataForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget())
    season = forms.ChoiceField(choices=SEASONS)
    holiday = forms.ChoiceField(widget=forms.RadioSelect, choices=MYBOOLEAN)
    weekday = forms.ChoiceField(choices=DAYS)
    workingday = forms.ChoiceField(choices=MYBOOLEAN)
    weathersit = forms.ChoiceField(choices=SITUATION)
    temp = forms.FloatField()
    atemp = forms.FloatField()
    hum = forms.FloatField()
    windspeed = forms.FloatField()
    # class Meta:
    #     fields=['day','mnth','year','season','holiday','weekday','workingday','weathersit','temp','atemp','hum','windspeed']

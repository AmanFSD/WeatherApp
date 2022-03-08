from django.forms import ModelForm, TextInput
from .models import WeatherData

class CityForm(ModelForm):
    class Meta:
        model = WeatherData
        fields = ['name','temp','description','icon','date']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder
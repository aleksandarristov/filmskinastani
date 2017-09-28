from django import forms
from django.forms import ModelForm
from .models import Movie
from .models import Actor
from .models import Award
from .models import Producent


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'

class AwardForm(ModelForm):
    class Meta:
        model = Award
        fields = '__all__'

class ProducentForm(ModelForm):
    class Meta:
        model = Producent
        fields = '__all__'
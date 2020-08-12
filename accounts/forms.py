from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text= "insira um email.")
    first_name = forms.CharField(required=True, help_text= "insira um nome.", label="Nome")

    class Meta:
        model = User
        fields =("username","first_name","email")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email já cadastrado.")
        return email


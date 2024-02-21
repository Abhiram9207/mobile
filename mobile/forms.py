from django import forms
from mobile.models import Mobiles
from django.contrib.auth.models import User



class MobileForm(forms.ModelForm):
    class Meta:
        model=Mobiles
        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "brand":forms.TextInput(attrs={"class":"form-control"}),
            "specs":forms.TextInput(attrs={"class":"form-control"}),
            "display":forms.TextInput(attrs={"class":"form-control"})

        }


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]


        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}),
            "email":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Email adderss"}),
            "password":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Password"})
        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=(forms.TextInput(attrs={"class":"form-control","placeholder":"enter username"})))
    password=forms.CharField(widget=(forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter password"})))

    

    #    widgets={
           
    #         "username":forms.TextInput(attrs={"class":"form-control","placeholder":"enterusername"})
    #         "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter password"})
    #    }






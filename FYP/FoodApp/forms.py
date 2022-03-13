from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import ReviewRating
from django.forms import ModelForm
from django.forms import TextInput,EmailInput,PasswordInput
# from .models import ReviewRating
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
    # then do extra stuff:
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Enter User Name'})
        self.fields['email'].widget= forms.EmailInput(attrs={'placeholder': 'Enter Your Mail'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Enter Your Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Your Password'})
       
    #     widgets = {
    #     'username': forms.TextInput(
    #         attrs = {
    #             'placeholder':'Enter User Name',
    #             'class': 'validate'
    #         },
    #     ),

    #     'email': forms.EmailInput(
    #         attrs = {
    #             'placeholder': 'Enter your E-mail',
    #             'class': 'validate'
    #         },
    #     ),

    #     'password1': forms.PasswordInput(
    #         attrs = {
    #             'placeholder': 'Password',
    #             'class': 'validate'
    #         },
    #     ),
    #     'password2': forms.PasswordInput(
    #         attrs = {
    #             'placeholder': 'Password',
    #             'class': 'validate'
    #         },
    #     ),

    # }
        # widgets = {
        #     'username': forms.TextInput(
        #         attrs={'placeholder': 'Enter Your Name', 'class': 'form-control'}),
        #     'email': forms.EmailInput(
        #         attrs={'placeholder': 'Enter Your Mail', 'class': 'form-control'}),
        #     'password1': forms.PasswordInput(
        #         attrs={'placeholder': 'Enter Your Password', 'class': 'form-control'}),
        #     'password2': forms.PasswordInput(
        #         attrs={'placeholder': 'Confirm Your Password', 'class': 'form-control'})
        # }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['review','comment', 'rate']

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,6)]
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce =int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
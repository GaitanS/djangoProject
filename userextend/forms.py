from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, CheckboxInput
from userextend.models import UserExtend


class UserExtendForm(UserCreationForm):
    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'is_adult', 'username']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first_name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last_name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email', 'class': 'form-control'}),
            'phone': TextInput(attrs={'placeholder': 'Please enter your phone number', 'class': 'form-control'}),
            'address': TextInput(attrs={'placeholder': 'Please enter your address', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Please enter your username', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserExtendForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter password confirmation'

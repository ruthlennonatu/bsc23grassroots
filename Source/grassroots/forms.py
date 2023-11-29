from django import forms
from .models import Person  # Adjust the import according to your project structure

'''Classes to connect the forms in the templates to the database models'''
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['userID', 'username', 'password', 'first_name', 'last_name', 'phone', 'address']
        widgets = {
            'password': forms.PasswordInput(),  # This makes the password field render as a password input
        }

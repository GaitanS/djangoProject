from django import forms
from django.forms import TextInput, Textarea, HiddenInput

from category.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        # fields = '__all__'
        fields = ['name', 'description', 'active']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter your name', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter your description', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].label = 'Numele tau'
        # self.fields['name'].widget = HiddenInput()

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Numele tau'
        # self.fields['name'].widget = HiddenInput()

    def clean(self):
        cleaned_data = self.cleaned_data
        name_input = cleaned_data.get('name')  # iau textul pe care il scriu in inputul name
        all_categories = Category.objects.all()  # interogam baza de date luand toate categoriile salvate in db
        for category in all_categories:  # parcurgem prin categoriile din db
            if name_input.lower() == category.name.lower():
                msg = 'This name of category already exist in db!'
                self._errors['name'] = self.error_class([msg])

        return cleaned_data

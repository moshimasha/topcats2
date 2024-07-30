from django import forms

class RecipeConvertForm(forms.Form):
    input_url = forms.URLField(label="Enter a URL")
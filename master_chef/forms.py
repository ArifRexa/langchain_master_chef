from django import forms

class MasterCheifForm(forms.Form):
    recipe_message = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Recipe message'}))

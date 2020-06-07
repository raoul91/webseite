from django import forms

class HomeForm(forms.Form):
    post = forms.CharField(label = 'Gib eine natürliche Zahl N ein:')

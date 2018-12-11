from django import forms


class AddArtForm(forms.Form):
    title = forms.CharField(min_length=5, required=True)
    desc = forms.CharField(min_length=20, required=True)
    content = forms.CharField(required=True)



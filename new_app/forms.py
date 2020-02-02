from django import forms


class PageForm(forms.Form):
    key = forms.CharField(
        max_length=9,
        widget=forms.TextInput(attrs={'placeholder': 'Certificate Number'})
    )

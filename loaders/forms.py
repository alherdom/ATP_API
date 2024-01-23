from django import forms


class UploadFilesForm(forms.Form):
    matches = forms.FileField()
    players = forms.FileField()
    stats = forms.FileField()

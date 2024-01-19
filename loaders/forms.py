from django import forms


class UploadFilesForm(forms.Form):
    match = forms.FileField()
    player = forms.FileField()
    stats = forms.FileField()

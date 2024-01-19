import csv
from .forms import UploadFilesForm
from django.shortcuts import render, redirect, get_list_or_404


def home(request):
    return redirect("loaders:upload_files")


def upload_files(request):
    if request.method == "POST":
        form = UploadFilesForm(request.POST, request.FILES)
        if form.is_valid():
            pass
    else:
        form = UploadFilesForm()
    return render(request, "loaders/upload.html", {"form": form})

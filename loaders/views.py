from .forms import UploadFilesForm
from .utils import handle_uploaded_file
from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return redirect("loaders:upload_files")


def upload_files(request):
    if request.method == "POST":
        form = UploadFilesForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            messages.success(request, "Files was successfully uploaded!")
        else:
            messages.error(request, "There are errors in form!")
        return render(request, "loaders/upload.html", {"form": form})
    else:
        form = UploadFilesForm()
    return render(request, "loaders/upload.html", {"form": form})

from .forms import UploadFilesForm
from .utils import handle_uploaded_file
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return redirect("loaders:upload_files")


@staff_member_required
def upload_files(request):
    if request.method == "POST":
        form = UploadFilesForm(request.POST, request.FILES)
        if form.is_valid():
            matches = request.FILES["matches"]
            players = request.FILES["players"]
            stats = request.FILES["stats"]
            handle_uploaded_file(matches, players, stats)
            return redirect("loaders:upload_ok")
    else:
        form = UploadFilesForm()
    return render(request, "loaders/upload.html", {"form": form})


def upload_ok(request):
    return render(request, "loaders/upload_ok.html")

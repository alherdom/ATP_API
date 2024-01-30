from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UploadFilesForm
from .utils import (
    handle_uploaded_players,
    handle_uploaded_matches,
    handle_uploaded_stats,
)


def home(request):
    return redirect("loaders:upload_files")


@staff_member_required
def upload_files(request):
    if request.method == "POST":
        form = UploadFilesForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_players(request.FILES["players"])
            handle_uploaded_matches(request.FILES["matches"])
            handle_uploaded_stats(request.FILES["stats"])
            return redirect("loaders:upload_ok")
    else:
        form = UploadFilesForm()
    return render(request, "loaders/upload.html", {"form": form})


def upload_ok(request):
    return render(request, "loaders/upload_ok.html")

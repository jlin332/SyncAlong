# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def displayMySongs(request):
    return render(request, "MySongs.html", {})

def displayUploadSongs(request):
    return render(request, "UploadSongs.html", {})

def displayCreatePlaylist(request):
    return render(request, "CreatePlaylist.html", {})

def displaUploadLyric(request):
    return render(request, "UploadLyric.html", {})

from django.shortcuts import render
from django.views.generic import DetailView

from .models import Entry
# Create your views here.

class EntryDetail(DetailView):
    model=Entry
    # template_name = '_entry.html'
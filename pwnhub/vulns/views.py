from django.shortcuts import render
from django.views.generic import ListView
from models import *


class AllVulnsListView(ListView):
    model = Vulnerability

from django.shortcuts import render
from core.models import Core


class CoreViews():

    model = Core
    template_name = 'base.html'

def getMaimPage(request):
    return render(request, 'mainPage.html')

def getErrorPage(request):
    return render(request, 'errorPage.html')

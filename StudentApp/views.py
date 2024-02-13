from django.shortcuts import render



def ShowHome(request):

    return render(request, "home.html")

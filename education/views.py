from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, "wrapper.html")


def dashboard(request):
    return render(request, "dashboard.html")


def datatables(request):
    return render(request, "data.html")

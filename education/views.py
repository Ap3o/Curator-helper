from django.shortcuts import render, HttpResponse
from .models import AcademicPerformance


def index(request):
    return render(request, "wrapper.html")


def dashboard(request):
    return render(request, "dashboard.html")


def datatables(request):
    academicperfomance = AcademicPerformance.objects.all()
    return render(request, "data.html", {"content": academicperfomance})

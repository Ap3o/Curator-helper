from django.views import generic
from django.shortcuts import render, HttpResponse
from . import models, forms


def index(request):
    return render(request, "wrapper.html")


def dashboard(request):
    return render(request, "dashboard.html")


def datatables(request):
    academic_performance = models.AcademicPerformance.objects.all()
    form = forms.AcademicPerformanceForm()
    return render(request, "academic_performance.html", {"content": academic_performance, "form": form})

# Неиспользуемый код.
# class AcademicPerformanceCreateView(generic.CreateView):
#     model = models.AcademicPerformance
#     form_class = forms.AcademicPerformanceForm
#     template_name = "academicperformance_form.html"
#     success_url = "/"

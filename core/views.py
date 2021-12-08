from django.contrib.auth import logout
from django.shortcuts import render, redirect
from education import models
from django.db.models import Count


# Create your views here.
def index(request):
    return render(request, "main.html")


def get_subject_name(subject_id):
    return models.Subject.objects.get(id=subject_id).name


def final_performance(request):
    objects = models.AcademicPerformance.objects \
        .values('subject', 'mark') \
        .filter(type_of_perfomance="Итоговая") \
        .order_by('subject') \
        .annotate(count=Count('mark'))

    data = dict()
    subject_id = objects[0]['subject']
    subject_name = get_subject_name(subject_id)
    data[subject_name] = {"labels": [], "datasets": []}
    for _object in objects:
        if subject_id != _object['subject']:
            subject_id = _object['subject']
            subject_name = get_subject_name(subject_id)
            data[subject_name] = {"labels": [], "datasets": []}
        data[subject_name]['labels'].append(str(_object['mark']))
        data[subject_name]['datasets'].append(_object['count'])
    return render(request, "dashboard.html", {"data": data})


def handler404(request, exception, template_name="page404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response


def handler500(request, template_name="page500.html"):
    response = render(request, template_name)
    response.status_code = 500
    return response


def logout_user(request):
    logout(request)
    return redirect("/")

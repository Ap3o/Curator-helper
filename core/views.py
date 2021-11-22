from django.shortcuts import render
from education import models
from django.db.models import Count


# Create your views here.
def index(request):
    return render(request, "wrapper.html")


def dashboard(request):
    objects = models.AcademicPerformance.objects.values('subject', 'mark').order_by('subject').annotate(
        count=Count('mark')
    )

    data = dict()
    subject_id = objects[0]['subject']
    data[subject_id] = {"labels": [], "datasets": []}
    for _object in objects:
        if subject_id != _object['subject']:
            break
            subject_id = _object['subject']
            data[subject_id] = dict()
        data[subject_id]['labels'].append(str(_object['mark']))
        data[subject_id]['datasets'].append(_object['count'])
    return render(request, "dashboard.html", {"data": data})

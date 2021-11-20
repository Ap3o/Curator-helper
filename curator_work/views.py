from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from . import models
from . import forms


def report(request):
    objects = models.Report.objects.all()
    return render(request, "tables/curator_work/report.html", {"content": objects})


def report_modal(request):
    if request.method == "GET":
        initial_id = request.GET.get("initial_id", '')
        if initial_id != '':
            # Если это запись для редактирования
            initial_model = models.Report.objects.get(id=initial_id)

            initial_data = {
                "content": initial_model.content,
                "start_at": initial_model.start_at,
                "end_at": initial_model.end_at,
            }
            form = forms.ReportForm(initial=initial_data)
            return render(request, "modals/curator_work/modalReport.html", {"form": form, 'initial_id': initial_id})
        else:
            form = forms.ReportForm()
            return render(request, "modals/curator_work/modalReport.html", {"form": form, 'initial_id': ''})


@require_http_methods(["GET"])
def report_delete(request):
    models.Report.objects.get(id=request.GET.get("id", '')).delete()
    return JsonResponse({"result": True, "text": "Запись удалена!"})


@require_http_methods(["POST"])
def report_edit(request, pk):
    model = models.Report.objects.get(id=pk)

    model.content = request.POST.get('content')
    model.start_at = request.POST.get('start_at')
    model.end_at = request.POST.get('end_at')

    model.save()
    return JsonResponse({"result": True, "text": "Запись обновлена!"})


@require_http_methods(["POST"])
def report_create(request):
    model = models.Report()

    model.content = request.POST.get('content')
    model.start_at = request.POST.get('start_at')
    model.end_at = request.POST.get('end_at')

    model.save()
    return JsonResponse({"result": True, "text": "Запись создана!"})


def parentteachermeeting(request):
    objects = models.ParentTeacherMeeting.objects.all()
    return render(request, "tables/curator_work/parentteachermeeting.html", {"content": objects})


def parentteachermeeting_modal(request):
    if request.method == "GET":
        initial_id = request.GET.get("initial_id", '')
        if initial_id != '':
            # Если это запись для редактирования
            initial_model = models.ParentTeacherMeeting.objects.get(id=initial_id)

            initial_data = {
                "content": initial_model.content,
                "date": initial_model.date,
            }
            form = forms.ParentTeacherMeetingForm(initial=initial_data)
            return render(request, "modals/curator_work/modalParentTeacherMeeting.html", {"form": form, 'initial_id': initial_id})
        else:
            form = forms.ParentTeacherMeetingForm()
            return render(request, "modals/curator_work/modalParentTeacherMeeting.html", {"form": form, 'initial_id': ''})


@require_http_methods(["GET"])
def parentteachermeeting_delete(request):
    models.ParentTeacherMeeting.objects.get(id=request.GET.get("id", '')).delete()
    return JsonResponse({"result": True, "text": "Запись удалена!"})


@require_http_methods(["POST"])
def parentteachermeeting_edit(request, pk):
    model = models.ParentTeacherMeeting.objects.get(id=pk)

    model.content = request.POST.get('content')
    model.date = request.POST.get('date')

    model.save()
    return JsonResponse({"result": True, "text": "Запись обновлена!"})


@require_http_methods(["POST"])
def parentteachermeeting_create(request):
    model = models.ParentTeacherMeeting()

    model.content = request.POST.get('content')
    model.date = request.POST.get('date')

    model.save()
    return JsonResponse({"result": True, "text": "Запись создана!"})


# educationalactivities
def educationalactivities(request):
    objects = models.EducationalActivities.objects.all()
    return render(request, "tables/curator_work/educationalactivities.html", {"content": objects})


def educationalactivities_modal(request):
    if request.method == "GET":
        initial_id = request.GET.get("initial_id", '')
        if initial_id != '':
            # Если это запись для редактирования
            initial_model = models.EducationalActivities.objects.get(id=initial_id)

            initial_data = {
                "activity": initial_model.activity,
                "date": initial_model.date,
                "note": initial_model.note,
            }
            form = forms.EducationalActivitiesForm(initial=initial_data)
            return render(request, "modals/curator_work/modalActivity.html", {"form": form, 'initial_id': initial_id})
        else:
            form = forms.EducationalActivitiesForm()
            return render(request, "modals/curator_work/modalActivity.html", {"form": form, 'initial_id': ''})


@require_http_methods(["GET"])
def educationalactivities_delete(request):
    models.EducationalActivities.objects.get(id=request.GET.get("id", '')).delete()
    return JsonResponse({"result": True, "text": "Запись удалена!"})


@require_http_methods(["POST"])
def educationalactivities_edit(request, pk):
    model = models.EducationalActivities.objects.get(id=pk)

    model.activity = request.POST.get('activity')
    model.date = request.POST.get('date')
    model.note = request.POST.get('note')

    model.save()
    return JsonResponse({"result": True, "text": "Запись обновлена!"})


@require_http_methods(["POST"])
def educationalactivities_create(request):
    model = models.EducationalActivities()

    model.activity = request.POST.get('activity')
    model.date = request.POST.get('date')
    model.note = request.POST.get('note')

    model.save()
    return JsonResponse({"result": True, "text": "Запись создана!"})

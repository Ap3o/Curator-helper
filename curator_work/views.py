from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from . import models
from . import forms


def process_the_request(request, model, form, table_link, save_model_func, get_initial_data_func):
    if request.method == "GET":
        objects = model.objects.all()
        return render(request, table_link, {"content": objects})

    if request.is_ajax():
        if request.method == "POST":

            if request.POST["type"] == "delete":
                model.objects.get(id=request.POST["id"]).delete()
                return JsonResponse({"result": True, "text": "Запись удалена!"})

            if request.POST["type"] == "get_modal":
                # Если id был передан, значит запись надо отредактировать. Если не передан - создать новую.
                if 'id' in request.POST:
                    _id = request.POST['id']
                    model_to_edit = model.objects.get(id=_id)
                    initial_data = get_initial_data_func(model_to_edit)
                    form = form(initial=initial_data)
                else:
                    _id = None
                    form = form()
                return render(request, "modals/modal.html", {"form": form, "id": _id})

            if request.POST["type"] == "save":
                if request.POST['id'] == 'None':
                    save_model = model()
                    text = "Запись добавлена!"
                else:
                    save_model = model.objects.get(id=request.POST['id'])
                    text = "Запись отредактирована!"

                save_model_func(save_model)
                return JsonResponse({"result": True, "text": text})


@require_http_methods(["GET", "POST"])
def report(request):
    def get_initial_data(_model):
        initial_data = {
            "content": _model.content,
            "start_at": _model.start_at,
            "end_at": _model.end_at,
        }
        return initial_data

    def save_model(_model):
        # Поля для изменения в каждой форме.
        _model.content = request.POST.get('content')
        _model.start_at = request.POST.get('start_at')
        _model.end_at = request.POST.get('end_at')
        _model.save()

    model = models.Report
    form = forms.ReportForm
    table_link = "tables/curator_work/report.html"
    return process_the_request(request, model, form, table_link, save_model, get_initial_data)


@require_http_methods(["GET", "POST"])
def educationalactivities(request):
    def get_initial_data(_model):
        initial_data = {
            "activity": _model.activity,
            "date": _model.date,
            "note": _model.note,
        }
        return initial_data

    def save_model(_model):
        # Поля для изменения в каждой форме.
        _model.activity = request.POST.get('activity')
        _model.date = request.POST.get('date')
        _model.note = request.POST.get('note')
        _model.save()

    model = models.EducationalActivities
    form = forms.EducationalActivitiesForm
    table_link = "tables/curator_work/educationalactivities.html"
    return process_the_request(request, model, form, table_link, save_model, get_initial_data)


@require_http_methods(["GET", "POST"])
def parentteachermeeting(request):
    def get_initial_data(_model):
        initial_data = {
            "content": _model.content,
            "date": _model.date,
        }
        return initial_data

    def save_model(_model):
        # Поля для изменения в каждой форме.
        _model.content = request.POST.get('content')
        _model.date = request.POST.get('date')
        _model.save()

    model = models.ParentTeacherMeeting
    form = forms.ParentTeacherMeetingForm
    table_link = "tables/curator_work/parentteachermeeting.html"
    return process_the_request(request, model, form, table_link, save_model, get_initial_data)

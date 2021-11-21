from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

from . import models
from . import forms


def process_the_request(request, model, form, table_link, save_model_func):
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
                    initial_data = {
                        "topic": model_to_edit.topic,
                        "month": model_to_edit.month,
                    }
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
def class_period(request):
    def save_model(_model):
        # Поля для изменения в каждой форме.
        _model.topic = request.POST.get('topic')
        _model.month = request.POST.get('month')
        _model.save()

    model = models.ClassPeriod
    form = forms.ClassPeriodForm
    table_link = "tables/homeroom/classperiod.html"
    return process_the_request(request, model, form, table_link, save_model)

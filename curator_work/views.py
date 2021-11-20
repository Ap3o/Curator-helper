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

from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from . import models, forms


def index(request):
    return render(request, "wrapper.html")


def dashboard(request):
    return render(request, "dashboard.html")


def student(request):
    objects = models.Student.objects.all()
    return render(request, "tables/students.html", {"content": objects})


def student_modal(request):
    if request.method == "GET":
        initial_id = request.GET.get("initial_id", '')
        if initial_id != '':
            # Если это запись для редактирования
            initial_model = models.Student.objects.get(id=initial_id)

            initial_data = {
                "full_name": initial_model.full_name,
                "date_of_birth": initial_model.date_of_birth,
                "home_address": initial_model.home_address,
            }
            form = forms.StudentForm(initial=initial_data)
            return render(request, "modals/modalStudent.html", {"form": form, 'initial_id': initial_id})
        else:
            form = forms.StudentForm()
            return render(request, "modals/modalStudent.html", {"form": form, 'initial_id': ''})


@require_http_methods(["GET"])
def student_delete(request):
    models.Student.objects.get(id=request.GET.get("id", '')).delete()
    return JsonResponse({"result": True, "text": "Запись удалена!"})


@require_http_methods(["POST"])
def student_edit(request, pk):
    model = models.Student.objects.get(id=pk)

    model.full_name = request.POST.get('full_name')
    model.date_of_birth = request.POST.get('date_of_birth')
    model.home_address = request.POST.get('home_address')

    model.save()
    return JsonResponse({"result": True, "text": "Запись обновлена!"})


@require_http_methods(["POST"])
def student_create(request):
    model = models.Student()

    model.full_name = request.POST.get('full_name')
    model.date_of_birth = request.POST.get('date_of_birth')
    model.home_address = request.POST.get('home_address')

    model.save()
    return JsonResponse({"result": True, "text": "Запись создана!"})


def academic_performance(request):
    academic_performance_objects = models.AcademicPerformance.objects.all()
    return render(request, "tables/academic_performance.html", {"content": academic_performance_objects})


def academic_performance_modal(request):
    if request.method == "GET":
        initial_id = request.GET.get("initial_id", '')
        if initial_id != '':
            # Если это запись для редактирования
            initial_academic_perf = models.AcademicPerformance.objects.get(id=initial_id)

            initial_data = {
                "student": initial_academic_perf.student.id,
                "teacher": initial_academic_perf.teacher.id,
                "subject": initial_academic_perf.subject.id,
                "type_of_perfomance": initial_academic_perf.type_of_perfomance,
                "mark": initial_academic_perf.mark
            }
            form = forms.AcademicPerformanceForm(initial=initial_data)
            return render(request, "modals/modalAcademicPerformance.html", {"form": form, 'initial_id': initial_id})
        else:
            form = forms.AcademicPerformanceForm()
            return render(request, "modals/modalAcademicPerformance.html", {"form": form, 'initial_id': ''})


@require_http_methods(["GET"])
def academic_performance_delete(request):
    models.AcademicPerformance.objects.get(id=request.GET.get("id", '')).delete()
    return JsonResponse({"result": True, "text": "Запись удалена!"})


@require_http_methods(["POST"])
def academic_performance_edit(request, pk):
    model = models.AcademicPerformance.objects.get(id=pk)

    set_fields_academic_performance(model, request)
    model.type_of_perfomance = request.POST.get('type_of_perfomance')
    model.mark = request.POST.get('mark')

    model.save()
    return JsonResponse({"result": True, "text": "Запись обновлена!"})


@require_http_methods(["POST"])
def academic_performance_create(request):
    model = models.AcademicPerformance()

    set_fields_academic_performance(model, request)
    model.type_of_perfomance = request.POST.get('type_of_perfomance')
    model.mark = request.POST.get('mark')

    model.save()
    return JsonResponse({"result": True, "text": "Запись создана!"})


def set_fields_academic_performance(model, request):
    model.student = models.Student.objects.get(id=request.POST.get('student'))
    model.teacher = models.Teacher.objects.get(id=request.POST.get('teacher'))
    model.subject = models.Subject.objects.get(id=request.POST.get('subject'))

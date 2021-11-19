from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from . import models, forms


def index(request):
    return render(request, "wrapper.html")


def dashboard(request):
    return render(request, "dashboard.html")


def performance(request):
    objects = models.Performance.objects.all()
    return render(request, "tables/education/performance.html", {"content": objects})


def performance_modal(request):
    if request.method == "GET":
        initial_id = request.GET.get("initial_id", '')
        if initial_id != '':
            # Если это запись для редактирования
            initial_model = models.Performance.objects.get(id=initial_id)

            initial_data = {
                "student": initial_model.student,
                "subject": initial_model.subject,
                "mark": initial_model.mark,
            }
            form = forms.PerformanceForm(initial=initial_data)
            return render(request, "modals/education/modalPerformance.html", {"form": form, 'initial_id': initial_id})
        else:
            form = forms.PerformanceForm()
            return render(request, "modals/education/modalPerformance.html", {"form": form, 'initial_id': ''})


@require_http_methods(["GET"])
def performance_delete(request):
    models.Performance.objects.get(id=request.GET.get("id", '')).delete()
    return JsonResponse({"result": True, "text": "Запись удалена!"})


@require_http_methods(["POST"])
def performance_edit(request, pk):
    model = models.Performance.objects.get(id=pk)

    model.student = models.Student.objects.get(id=request.POST.get('student'))
    model.subject = models.Subject.objects.get(id=request.POST.get('subject'))
    model.mark = request.POST.get('mark')

    model.save()
    return JsonResponse({"result": True, "text": "Запись обновлена!"})


@require_http_methods(["POST"])
def performance_create(request):
    model = models.Performance()
    print(request.POST)
    model.student = models.Student.objects.get(id=request.POST.get('student'))
    model.subject = models.Subject.objects.get(id=request.POST.get('subject'))
    model.mark = request.POST.get('mark')

    model.save()
    return JsonResponse({"result": True, "text": "Запись создана!"})


def hobbies(request):
    objects = models.Hobbies.objects.all()
    return render(request, "tables/education/hobbies.html", {"content": objects})


def hobbies_modal(request):
    if request.method == "GET":
        initial_id = request.GET.get("initial_id", '')
        if initial_id != '':
            # Если это запись для редактирования
            initial_model = models.Hobbies.objects.get(id=initial_id)

            initial_data = {
                "student": initial_model.student,
                "hobby": initial_model.hobby,
            }
            form = forms.HobbiesForm(initial=initial_data)
            return render(request, "modals/education/modalHobbies.html", {"form": form, 'initial_id': initial_id})
        else:
            form = forms.HobbiesForm()
            return render(request, "modals/education/modalHobbies.html", {"form": form, 'initial_id': ''})


@require_http_methods(["GET"])
def hobbies_delete(request):
    models.Hobbies.objects.get(id=request.GET.get("id", '')).delete()
    return JsonResponse({"result": True, "text": "Запись удалена!"})


@require_http_methods(["POST"])
def hobbies_edit(request, pk):
    model = models.Hobbies.objects.get(id=pk)

    model.hobby = request.POST.get('hobby')
    model.student = models.Student.objects.get(id=request.POST.get('student'))

    model.save()
    return JsonResponse({"result": True, "text": "Запись обновлена!"})


@require_http_methods(["POST"])
def hobbies_create(request):
    model = models.Hobbies()

    model.hobby = request.POST.get('hobby')
    model.student = models.Student.objects.get(id=request.POST.get('student'))
    model.save()
    return JsonResponse({"result": True, "text": "Запись создана!"})


def subjects(request):
    objects = models.Subject.objects.all()
    return render(request, "tables/education/subjects.html", {"content": objects})


def subjects_modal(request):
    if request.method == "GET":
        initial_id = request.GET.get("initial_id", '')
        if initial_id != '':
            # Если это запись для редактирования
            initial_model = models.Subject.objects.get(id=initial_id)

            initial_data = {
                "name": initial_model.name,
                "teacher": initial_model.teacher,
            }
            form = forms.SubjectForm(initial=initial_data)
            return render(request, "modals/education/modalSubjects.html", {"form": form, 'initial_id': initial_id})
        else:
            form = forms.SubjectForm()
            return render(request, "modals/education/modalSubjects.html", {"form": form, 'initial_id': ''})


@require_http_methods(["GET"])
def subjects_delete(request):
    models.Subject.objects.get(id=request.GET.get("id", '')).delete()
    return JsonResponse({"result": True, "text": "Запись удалена!"})


@require_http_methods(["POST"])
def subjects_edit(request, pk):
    model = models.Subject.objects.get(id=pk)

    model.name = request.POST.get('name')
    model.teacher = models.Teacher.objects.get(id=request.POST.get('teacher'))

    model.save()
    return JsonResponse({"result": True, "text": "Запись обновлена!"})


@require_http_methods(["POST"])
def subjects_create(request):
    model = models.Subject()

    model.name = request.POST.get('name')
    model.teacher = models.Teacher.objects.get(id=request.POST.get('teacher'))

    model.save()
    return JsonResponse({"result": True, "text": "Запись создана!"})


def parents(request):
    objects = models.Parent.objects.all()
    return render(request, "tables/education/parents.html", {"content": objects})


def parents_modal(request):
    if request.method == "GET":
        initial_id = request.GET.get("initial_id", '')
        if initial_id != '':
            # Если это запись для редактирования
            initial_model = models.Parent.objects.get(id=initial_id)

            initial_data = {
                "full_name": initial_model.full_name,
                "place_of_work": initial_model.place_of_work,
                "phone_number": initial_model.phone_number,
                # TODO
                # "student": initial_model.student
            }
            form = forms.ParentsForm(initial=initial_data)
            return render(request, "modals/education/modalParents.html", {"form": form, 'initial_id': initial_id})
        else:
            form = forms.ParentsForm()
            return render(request, "modals/education/modalParents.html", {"form": form, 'initial_id': ''})


@require_http_methods(["GET"])
def parents_delete(request):
    models.Parent.objects.get(id=request.GET.get("id", '')).delete()
    return JsonResponse({"result": True, "text": "Запись удалена!"})


@require_http_methods(["POST"])
def parents_edit(request, pk):
    model = models.Parent.objects.get(id=pk)

    model.full_name = request.POST.get('full_name')
    model.place_of_work = request.POST.get('place_of_work')
    model.phone_number = request.POST.get('phone_number')
    # TODO
    # model.student = request.POST.get('student')

    model.save()
    return JsonResponse({"result": True, "text": "Запись обновлена!"})


@require_http_methods(["POST"])
def parents_create(request):
    model = models.Parent()

    model.full_name = request.POST.get('full_name')
    model.place_of_work = request.POST.get('place_of_work')
    model.phone_number = request.POST.get('phone_number')
    # TODO
    # print(request.POST.get('student'))
    # model.student = request.POST.get('student')

    model.save()
    return JsonResponse({"result": True, "text": "Запись создана!"})


def teachers(request):
    objects = models.Teacher.objects.all()
    return render(request, "tables/education/teachers.html", {"content": objects})


def teachers_modal(request):
    if request.method == "GET":
        initial_id = request.GET.get("initial_id", '')
        if initial_id != '':
            # Если это запись для редактирования
            initial_model = models.Teacher.objects.get(id=initial_id)

            initial_data = {
                "full_name": initial_model.full_name,
                "department": initial_model.department,
            }
            form = forms.TeachersForm(initial=initial_data)
            return render(request, "modals/education/modalTeachers.html", {"form": form, 'initial_id': initial_id})
        else:
            form = forms.TeachersForm()
            return render(request, "modals/education/modalTeachers.html", {"form": form, 'initial_id': ''})


@require_http_methods(["GET"])
def teachers_delete(request):
    models.Teacher.objects.get(id=request.GET.get("id", '')).delete()
    return JsonResponse({"result": True, "text": "Запись удалена!"})


@require_http_methods(["POST"])
def teachers_edit(request, pk):
    model = models.Teacher.objects.get(id=pk)

    model.full_name = request.POST.get('full_name')
    model.department = request.POST.get('department')

    model.save()
    return JsonResponse({"result": True, "text": "Запись обновлена!"})


@require_http_methods(["POST"])
def teachers_create(request):
    model = models.Teacher()

    model.full_name = request.POST.get('full_name')
    model.department = request.POST.get('department')

    model.save()
    return JsonResponse({"result": True, "text": "Запись создана!"})


def student(request):
    objects = models.Student.objects.all()
    return render(request, "tables/education/students.html", {"content": objects})


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
            return render(request, "modals/education/modalStudent.html", {"form": form, 'initial_id': initial_id})
        else:
            form = forms.StudentForm()
            return render(request, "modals/education/modalStudent.html", {"form": form, 'initial_id': ''})


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
    academic_performance_objects = models.AcademicPerformance.objects.all().select_related("student").select_related("teacher").select_related("subject")
    return render(request, "tables/education/academic_performance.html", {"content": academic_performance_objects})


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
            return render(request, "modals/education/modalAcademicPerformance.html", {"form": form, 'initial_id': initial_id})
        else:
            form = forms.AcademicPerformanceForm()
            return render(request, "modals/education/modalAcademicPerformance.html", {"form": form, 'initial_id': ''})


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

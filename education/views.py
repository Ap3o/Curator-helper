from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from . import models, forms


def index(request):
    return render(request, "wrapper.html")


def dashboard(request):
    return render(request, "dashboard.html")


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
def students(request):
    def get_initial_data(_model):
        initial_data = {
            "full_name": _model.full_name,
            "date_of_birth": _model.date_of_birth,
            "home_address": _model.home_address,
        }
        return initial_data

    def save_model(_model):
        # Поля для изменения в каждой форме.
        _model.full_name = request.POST.get('full_name')
        _model.date_of_birth = request.POST.get('date_of_birth')
        _model.home_address = request.POST.get('home_address')
        _model.save()

    model = models.Student
    form = forms.StudentForm
    table_link = "tables/education/students.html"
    return process_the_request(request, model, form, table_link, save_model, get_initial_data)


@require_http_methods(["GET", "POST"])
def parents(request):
    def get_initial_data(_model):
        initial_data = {
            "full_name": _model.full_name,
            "place_of_work": _model.place_of_work,
            "phone_number": _model.phone_number,
            # TODO ManyToManyField
        }
        return initial_data

    def save_model(_model):
        # Поля для изменения в каждой форме.
        _model.full_name = request.POST.get('full_name')
        _model.place_of_work = request.POST.get('place_of_work')
        _model.phone_number = request.POST.get('phone_number')
        _model.save()

    model = models.Parent
    form = forms.ParentsForm
    table_link = "tables/education/parents.html"
    return process_the_request(request, model, form, table_link, save_model, get_initial_data)


@require_http_methods(["GET", "POST"])
def hobbies(request):
    def get_initial_data(_model):
        initial_data = {
            "student": _model.student,
            "hobby": _model.hobby,
        }
        return initial_data

    def save_model(_model):
        # Поля для изменения в каждой форме.
        _model.student = models.Student.objects.get(id=request.POST.get('student'))
        _model.hobby = request.POST.get('hobby')
        _model.save()

    model = models.Hobbies
    form = forms.HobbiesForm
    table_link = "tables/education/hobbies.html"
    return process_the_request(request, model, form, table_link, save_model, get_initial_data)


@require_http_methods(["GET", "POST"])
def teachers(request):
    def get_initial_data(_model):
        initial_data = {
            "full_name": _model.full_name,
            "department": _model.department,
        }
        return initial_data

    def save_model(_model):
        # Поля для изменения в каждой форме.
        _model.full_name = request.POST.get('full_name')
        _model.department = request.POST.get('department')
        _model.save()

    model = models.Teacher
    form = forms.TeachersForm
    table_link = "tables/education/teachers.html"
    return process_the_request(request, model, form, table_link, save_model, get_initial_data)


@require_http_methods(["GET", "POST"])
def subjects(request):
    def get_initial_data(_model):
        initial_data = {
            "name": _model.name,
            "teacher": _model.teacher,
        }
        return initial_data

    def save_model(_model):
        # Поля для изменения в каждой форме.
        _model.name = request.POST.get('name')
        _model.teacher = models.Teacher.objects.get(id=request.POST.get('teacher'))
        _model.save()

    model = models.Subject
    form = forms.SubjectForm
    table_link = "tables/education/subjects.html"
    return process_the_request(request, model, form, table_link, save_model, get_initial_data)


@require_http_methods(["GET", "POST"])
def performance(request):
    def get_initial_data(_model):
        initial_data = {
            "student": _model.student,
            "subject": _model.subject,
            "mark": _model.mark,
        }
        return initial_data

    def save_model(_model):
        # Поля для изменения в каждой форме.
        _model.student = models.Student.objects.get(id=request.POST.get('student'))
        _model.subject = models.Subject.objects.get(id=request.POST.get('subject'))
        _model.mark = request.POST.get('mark')
        _model.save()

    model = models.Performance
    form = forms.PerformanceForm
    table_link = "tables/education/performance.html"
    return process_the_request(request, model, form, table_link, save_model, get_initial_data)


@require_http_methods(["GET", "POST"])
def academic_performance(request):
    def get_initial_data(_model):
        initial_data = {
            "student": _model.student,
            "subject": _model.subject,
            "teacher": _model.teacher,
            "type_of_perfomance": _model.type_of_perfomance,
            "mark": _model.mark,
        }
        return initial_data

    def save_model(_model):
        # Поля для изменения в каждой форме.
        _model.student = models.Student.objects.get(id=request.POST.get('student'))
        _model.subject = models.Subject.objects.get(id=request.POST.get('subject'))
        _model.teacher = models.Teacher.objects.get(id=request.POST.get('teacher'))
        _model.type_of_perfomance = request.POST.get('type_of_perfomance')
        _model.mark = request.POST.get('mark')
        _model.save()

    model = models.AcademicPerformance
    form = forms.AcademicPerformanceForm
    table_link = "tables/education/academic_performance.html"
    return process_the_request(request, model, form, table_link, save_model, get_initial_data)

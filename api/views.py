from django.http import JsonResponse
from education.models import Student, Subject, Teacher, AcademicPerformance


def index(request):
    students = Student.objects.filter(full_name__contains=request.GET.get('term', ''))
    students_array = [{'id': student.id, 'text': student.full_name} for student in students]
    return JsonResponse({'results': students_array})


def search_for_one_student(request):
    student_id = request.GET.get('term', '')
    student_name = Student.objects.get(id=request.GET.get('term', '')).full_name
    student = [{'id': student_id, 'text': student_name}]
    return JsonResponse({'results': student})


def get_subjects(request):
    subjects = Subject.objects.filter(name__contains=request.GET.get('term', ''))
    subjects_array = [{'id': subject.id, 'text': subject.name} for subject in subjects]
    return JsonResponse({'results': subjects_array})


def get_teachers(request):
    teachers = Teacher.objects.filter(full_name__contains=request.GET.get('term', ''))
    teachers_array = [{'id': teacher.id, 'text': teacher.full_name} for teacher in teachers]
    return JsonResponse({'results': teachers_array})


def get_academic_performance(request):
    academic_performance = AcademicPerformance.objects.get(id=request.GET.get('term', ''))
    return JsonResponse({
                         'student_name': academic_performance.student.full_name,
                         'teacher_name': academic_performance.teacher.full_name,
                         'subject_name': academic_performance.subject.name,
                         'type': academic_performance.type_of_perfomance,
                         'mark': academic_performance.mark
                         })

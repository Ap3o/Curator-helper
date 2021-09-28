from django.http import JsonResponse
from education.models import Student


def index(request):
    students = Student.objects.filter(full_name__contains=request.GET.get('term', ''))
    students_array = [{'id': student.id, 'text': student.full_name} for student in students]
    return JsonResponse({'results': students_array})


def search_for_one_student(request):
    student_id = request.GET.get('term', '')
    student_name = Student.objects.get(id=request.GET.get('term', '')).full_name
    student = [{'id': student_id, 'text': student_name}]
    return JsonResponse({'results': student})

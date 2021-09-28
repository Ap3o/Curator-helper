from django.http import JsonResponse
from education.models import Student


def index(request):
    students = Student.objects.filter(full_name__contains=request.GET.get('term', ''))
    students_array = [{'id': student.id, 'text': student.full_name} for student in students]
    return JsonResponse({'results': students_array})

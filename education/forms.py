from django import forms
from django_select2 import forms as s2forms

from . import models


class StudentWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "full_name__icontains",
    ]


class TeacherWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "full_name__icontains",
    ]


class SubjectWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "name__icontains",
    ]


class AcademicPerformanceWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "full_name__icontains",
        "type_of_perfomance__icontains",
        "mark__icontains",
    ]


class AcademicPerformanceForm(forms.ModelForm):
    class Meta:
        model = models.AcademicPerformance
        fields = "__all__"
        widgets = {
            "student": StudentWidget,
            "subject": SubjectWidget,
            "teacher": TeacherWidget
        }

    def __init__(self, *args, **kwargs):
        super(AcademicPerformanceForm, self).__init__(*args, **kwargs)

        # class
        self.fields["student"].widget.attrs.update({"class": "form-control select2"})
        self.fields["subject"].widget.attrs.update({"class": "form-control select2"})
        self.fields["teacher"].widget.attrs.update({"class": "form-control select2"})
        self.fields["type_of_perfomance"].widget.attrs.update({"class": "form-control select2"})
        self.fields["mark"].widget.attrs.update({"class": "form-control select2"})

        # style
        self.fields["student"].widget.attrs.update({"style": "width: 100%"})
        self.fields["subject"].widget.attrs.update({"style": "width: 100%"})
        self.fields["teacher"].widget.attrs.update({"style": "width: 100%"})
        self.fields["type_of_perfomance"].widget.attrs.update({"style": "width: 100%"})
        self.fields["mark"].widget.attrs.update({"style": "width: 100%"})

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


class PerformanceForm(forms.ModelForm):
    class Meta:
        model = models.Performance
        fields = "__all__"
        widgets = {
            "student": StudentWidget,
            "subject": SubjectWidget
        }

    def __init__(self, *args, **kwargs):
        super(PerformanceForm, self).__init__(*args, **kwargs)

        # class
        self.fields["student"].widget.attrs.update({"class": "form-control select2"})
        self.fields["subject"].widget.attrs.update({"class": "form-control select2"})
        self.fields["mark"].widget.attrs.update({"class": "form-control select2"})

        # style
        self.fields["student"].widget.attrs.update({"style": "width: 100%"})
        self.fields["subject"].widget.attrs.update({"style": "width: 100%"})
        self.fields["mark"].widget.attrs.update({"style": "width: 100%"})


class HobbiesForm(forms.ModelForm):
    class Meta:
        model = models.Hobbies
        fields = "__all__"
        widgets = {
            "student": StudentWidget
        }

    def __init__(self, *args, **kwargs):
        super(HobbiesForm, self).__init__(*args, **kwargs)

        # class
        self.fields["student"].widget.attrs.update({"class": "form-control select2"})
        self.fields["hobby"].widget.attrs.update({"class": "form-control select2"})

        # style
        self.fields["student"].widget.attrs.update({"style": "width: 100%"})
        self.fields["hobby"].widget.attrs.update({"style": "width: 100%"})


class ParentsForm(forms.ModelForm):
    class Meta:
        model = models.Parent
        fields = "__all__"
        # TODO решить проблему с ManyToMany
        widgets = {
            "student": StudentWidget
        }

    def __init__(self, *args, **kwargs):
        super(ParentsForm, self).__init__(*args, **kwargs)

        # class
        self.fields["full_name"].widget.attrs.update({"class": "form-control select2"})
        self.fields["place_of_work"].widget.attrs.update({"class": "form-control select2"})
        self.fields["phone_number"].widget.attrs.update({"class": "form-control select2"})
        self.fields["student"].widget.attrs.update({"class": "form-control select2"})

        # style
        self.fields["full_name"].widget.attrs.update({"style": "width: 100%"})
        self.fields["place_of_work"].widget.attrs.update({"style": "width: 100%"})
        self.fields["phone_number"].widget.attrs.update({"style": "width: 100%"})
        self.fields["student"].widget.attrs.update({"style": "width: 100%"})


class SubjectForm(forms.ModelForm):
    class Meta:
        model = models.Subject
        fields = "__all__"
        widgets = {
            "teacher": TeacherWidget
        }

    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)

        # class
        self.fields["name"].widget.attrs.update({"class": "form-control select2"})
        self.fields["teacher"].widget.attrs.update({"class": "form-control select2"})

        # style
        self.fields["name"].widget.attrs.update({"style": "width: 100%"})
        self.fields["teacher"].widget.attrs.update({"style": "width: 100%"})


class TeachersForm(forms.ModelForm):
    class Meta:
        model = models.Teacher
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TeachersForm, self).__init__(*args, **kwargs)

        # class
        self.fields["full_name"].widget.attrs.update({"class": "form-control select2"})
        self.fields["department"].widget.attrs.update({"class": "form-control select2"})

        # style
        self.fields["full_name"].widget.attrs.update({"style": "width: 100%"})
        self.fields["department"].widget.attrs.update({"style": "width: 100%"})


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        # class
        self.fields["full_name"].widget.attrs.update({"class": "form-control select2"})
        self.fields["date_of_birth"].widget.attrs.update({"class": "form-control select2"})
        self.fields["home_address"].widget.attrs.update({"class": "form-control select2"})

        # style
        self.fields["full_name"].widget.attrs.update({"style": "width: 100%"})
        self.fields["date_of_birth"].widget.attrs.update({"style": "width: 100%"})
        self.fields["home_address"].widget.attrs.update({"style": "width: 100%"})


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

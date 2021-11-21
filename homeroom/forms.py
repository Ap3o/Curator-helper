from django import forms
from django_select2 import forms as s2forms

from . import models


class ClassPeriodForm(forms.ModelForm):
    class Meta:
        model = models.ClassPeriod
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ClassPeriodForm, self).__init__(*args, **kwargs)

        # class
        self.fields["topic"].widget.attrs.update({"class": "form-control"})
        self.fields["month"].widget.attrs.update({"class": "form-control select2"})

        # style
        self.fields["topic"].widget.attrs.update({"style": "width: 100%"})
        self.fields["month"].widget.attrs.update({"style": "width: 100%"})


class ClassPeriodWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "topic__icontains",
    ]


class SpentClassPeriodForm(forms.ModelForm):
    class Meta:
        model = models.SpentClassPeriod
        fields = "__all__"
        widgets = {
            "class_period": ClassPeriodWidget
        }

    def __init__(self, *args, **kwargs):
        super(SpentClassPeriodForm, self).__init__(*args, **kwargs)

        # class
        self.fields["class_period"].widget.attrs.update({"class": "form-control select2"})
        self.fields["content"].widget.attrs.update({"class": "form-control"})

        # style
        self.fields["class_period"].widget.attrs.update({"style": "width: 100%"})
        self.fields["content"].widget.attrs.update({"style": "width: 100%"})

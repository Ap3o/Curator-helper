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

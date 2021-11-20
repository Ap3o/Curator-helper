from django import forms
from django_select2 import forms as s2forms

from . import models


class ReportForm(forms.ModelForm):
    class Meta:
        model = models.Report
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)

        # class
        self.fields["content"].widget.attrs.update({"class": "form-control"})
        self.fields["start_at"].widget.attrs.update({"class": "form-control"})
        self.fields["end_at"].widget.attrs.update({"class": "form-control"})

        # style
        self.fields["content"].widget.attrs.update({"style": "width: 100%"})
        self.fields["start_at"].widget.attrs.update({"style": "width: 100%"})
        self.fields["end_at"].widget.attrs.update({"style": "width: 100%"})
        # TODO исправить маски
        self.fields["start_at"].widget.attrs.update({"data-inputmask-alias": "datetime"})
        self.fields["start_at"].widget.attrs.update({"data-inputmask-inputformat": "dd/mm/yyyy"})
        self.fields["end_at"].widget.attrs.update({"data-inputmask-alias": "datetime"})
        self.fields["end_at"].widget.attrs.update({"data-inputmask-inputformat": "dd/mm/yyyy"})


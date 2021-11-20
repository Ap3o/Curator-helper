from django import forms
from django_select2 import forms as s2forms

from . import models


class ParentTeacherMeetingForm(forms.ModelForm):
    class Meta:
        model = models.ParentTeacherMeeting
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ParentTeacherMeetingForm, self).__init__(*args, **kwargs)

        # class
        self.fields["content"].widget.attrs.update({"class": "form-control"})
        self.fields["date"].widget.attrs.update({"class": "form-control"})

        # style
        self.fields["content"].widget.attrs.update({"style": "width: 100%"})
        self.fields["date"].widget.attrs.update({"style": "width: 100%"})

        # TODO Date input mask


class EducationalActivitiesForm(forms.ModelForm):
    class Meta:
        model = models.EducationalActivities
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EducationalActivitiesForm, self).__init__(*args, **kwargs)

        # class
        self.fields["activity"].widget.attrs.update({"class": "form-control"})
        self.fields["date"].widget.attrs.update({"class": "form-control"})
        self.fields["note"].widget.attrs.update({"class": "form-control"})

        # style
        self.fields["activity"].widget.attrs.update({"style": "width: 100%"})
        self.fields["date"].widget.attrs.update({"style": "width: 100%"})
        self.fields["note"].widget.attrs.update({"style": "width: 100%"})

        # TODO Date input mask


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

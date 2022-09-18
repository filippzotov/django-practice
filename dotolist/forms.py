from django.forms import ModelForm
from .models import Tasks
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ["title", "text", "start_time", "end_time"]
        widgets = {
            "start_time": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "end_time": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(TaskForm, self).__init__(*args, **kwargs)
    #     self.fields["title"].widget.attrs.update({"class": "form-control"})
    #     self.fields["text"].widget.attrs.update({"class": "form-control"})
    #     self.fields["start_time"].widget.attrs.update({"type": "datetime-local"})
    #     self.fields["end_time"].widget.attrs.update({"type": "datetime-local"})
    #     self.fields["start_time"].widget.attrs.update({"class": "form-control"})
    #     self.fields["end_time"].widget.attrs.update({"class": "form-control"})

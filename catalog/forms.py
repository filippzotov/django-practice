from turtle import textinput
from django import forms
from .models import News


class CommentForm(forms.Form):
    text = forms.CharField(
        label="Comment",
        max_length=300,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": "3",
            }
        ),
    )


# class NewsForm(forms.Form):
#     name = forms.CharField(label="Заголовок", max_length=50)
#     text = forms.CharField(label="Текст", widget=forms.Textarea)
#     photo = forms.ImageField(label="Изображение")


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["name", "text", "photo"]

    # widgets = {
    #     "name": forms.TextInput(attrs={"class": "form-control"}),
    #     "text": forms.Textarea(attrs={"class": "form-control", "rows": "10"}),
    #     "photo": forms.ImageField(attrs={"class": "form-control-file"}),
    # }
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["text"].widget.attrs.update({"class": "form-control"})
        self.fields["text"].widget.attrs.update({"rows": "10"})
        self.fields["photo"].widget.attrs.update({"class": "form-control-file"})

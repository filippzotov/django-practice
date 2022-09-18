from django import forms
from .models import PCpiece


class PCForm(forms.Form):

    CPU = forms.ModelChoiceField(
        queryset=PCpiece.objects.filter(typeitem__type="CPU"),
        empty_label=None,
    )
    GPU = forms.ModelChoiceField(
        queryset=PCpiece.objects.filter(typeitem__type="GPU"),
        empty_label=None,
    )
    RAM = forms.ModelChoiceField(
        queryset=PCpiece.objects.filter(typeitem__type="RAM"),
        empty_label=None,
    )
    case = forms.ModelChoiceField(
        queryset=PCpiece.objects.filter(typeitem__type="Case"),
        empty_label=None,
    )
    block = forms.ModelChoiceField(
        queryset=PCpiece.objects.filter(typeitem__type="Block"),
        empty_label=None,
    )
    motherboard = forms.ModelChoiceField(
        queryset=PCpiece.objects.filter(typeitem__type="Motherboard"),
        empty_label=None,
    )


class PieceForm(forms.Form):
    name = forms.CharField(max_length=200)


# class CommentForm(forms.Form):
#     text = forms.CharField(
#         label="Comment",
#         max_length=300,
#         widget=forms.Textarea(
#             attrs={
#                 "class": "form-control",
#                 "rows": "3",
#             }
#         ),
#     )


# class NewsForm(forms.Form):
#     name = forms.CharField(label="Заголовок", max_length=50)
#     text = forms.CharField(label="Текст", widget=forms.Textarea)
#     photo = forms.ImageField(label="Изображение")


# class NewsForm(forms.ModelForm):
#     class Meta:
#         model = News
#         fields = ["name", "text", "photo"]

# widgets = {
#     "name": forms.TextInput(attrs={"class": "form-control"}),
#     "text": forms.Textarea(attrs={"class": "form-control", "rows": "10"}),
#     "photo": forms.ImageField(attrs={"class": "form-control-file"}),
# }
#     def __init__(self, *args, **kwargs):
#         super(NewsForm, self).__init__(*args, **kwargs)
#         self.fields["name"].widget.attrs.update({"class": "form-control"})
#         self.fields["text"].widget.attrs.update({"class": "form-control"})
#         self.fields["text"].widget.attrs.update({"rows": "10"})
#         self.fields["photo"].widget.attrs.update({"class": "form-control-file"})

from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Console, Company, News, Comments
from django.views import generic
from .forms import *
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.db.models import F

# Create your views here.
from .models import PhotoOfPeople, SeriesOfPhotoShoots


def index(request):
    news = News.objects.all()
    # paginator = Paginator()
    context = {"news": news}

    return render(request, "catalog/index.html", context)


def consoles(request):
    companys = Company.objects.all()
    consoles = Console.objects.all()
    print(SeriesOfPhotoShoots.objects.filter(photoofpeople=None))
    # print(SeriesOfPhotoShoots.objects.exclude(pk=F("photoofpeople")))
    # test = Company.objects.exclude(pk=F("console__company__id"))
    # print(F("console__company_id"))
    context = {
        "consoles": consoles,
        "companys": companys,
    }
    return render(request, "catalog/consoles.html", context)


def company_consoles(request, company_id):
    companys = Company.objects.all()
    consoles = Console.objects.filter(company=company_id)

    context = {
        "consoles": consoles,
        "companys": companys,
    }
    return render(request, "catalog/consoles.html", context)


def make_news(request):
    newsform = NewsForm()
    context = {"newsform": newsform}
    print(request.method)
    print(request.FILES)
    if request.method == "POST" and request.FILES:
        print("hello")
        name = request.POST.get("name")
        text = request.POST.get("text")
        photo = request.FILES["photo"]
        print(photo)
        news = News(name=name, text=text, photo=photo)
        news.save()
        return HttpResponseRedirect("/")
    return render(request, "catalog/make_news.html", context)


class ConsoleDetailView(generic.DetailView):
    model = Console


def detail_comment(request, pk):
    news = News.objects.get(pk=pk)
    comment_form = CommentForm()
    if request.method == "POST":
        user = request.user
        # name = request.POST.get("name")
        text = request.POST.get("text")
        comment = Comments(user=user, text=text, news=news)
        comment.save()
        return HttpResponseRedirect(reverse("news-detail", args=[pk]))
    else:
        context = {"comment_form": comment_form, "news": news}
        return render(request, "catalog/news_detail.html", context)


# class NewsDetailView(generic.DetailView):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["comment_form"] = CommentForm()
#         return context

#     def get(self, request, *args, **kwargs):

#         self.object = self.get_object()
#         context = self.get_context_data(object=self.object)
#         if request.method == "POST":
#             name = request.POST.get("name")
#             text = request.POST.get("text")
#             print(name, text)
#         return self.render_to_response(context)

#     model = News

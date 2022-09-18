from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Genre(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Введите название жанра",
        verbose_name="Жанр игры",
    )

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Введите название игры",
        verbose_name="Название игры",
    )
    release_date = models.DateField(
        help_text="Введите дату выхода игры",
        verbose_name="Дата выхода игры",
        null=True,
        blank=True,
    )
    picture = models.ImageField(upload_to="games/", default="...")

    genre = models.ForeignKey(
        "Genre",
        on_delete=models.CASCADE,
        help_text="Выберите жанр игры",
        verbose_name="Жанр игры",
        null=True,
        blank=True,
    )

    console = models.ForeignKey(
        "Console",
        on_delete=models.CASCADE,
        help_text="Выберите консоль",
        verbose_name="Консоль",
        null=True,
    )

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Введите название компании",
        verbose_name="Название компании",
    )
    country = models.CharField(
        max_length=50,
        help_text="Введите страну компании",
        verbose_name="Страна",
    )

    logo = models.ImageField(upload_to="logo/", default="...")

    def __str__(self):
        return self.name


class Console(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Введите название консоли",
        verbose_name="Название консоли",
    )
    release_date = models.DateField(
        help_text="Введите дату выхода консоли",
        verbose_name="Дата выхода консоли",
        null=True,
        blank=True,
    )
    company = models.ForeignKey(
        "Company",
        on_delete=models.CASCADE,
        help_text="Выберите компанию",
        verbose_name="Компания",
        null=True,
    )
    photo = models.ImageField(upload_to="consoles/", default="...")

    text = models.TextField(
        help_text="Введите описание консоли",
        verbose_name="Описание консоли",
        null=True,
    )

    def get_absolute_url(self):
        return reverse("console-detail", args=[str(self.id)])

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(
        max_length=50,
        help_text="Введите название консоли",
        verbose_name="Название консоли",
    )
    publish_date = models.DateField(auto_now_add=True)

    text = models.TextField(
        help_text="Введите описание консоли",
        verbose_name="Описание консоли",
        null=True,
        blank=True,
    )

    photo = models.ImageField(
        upload_to="news/",
        default="...",
        null=True,
        blank=True,
    )

    def get_absolute_url(self):
        return reverse("news-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = [
            "-pk",
        ]


class Comments(models.Model):
    # user = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    text = models.CharField(max_length=300)

    date_time = models.DateTimeField(auto_now_add=True)

    news = models.ForeignKey(
        "News",
        on_delete=models.CASCADE,
    )


class SeriesOfPhotoShoots(models.Model):
    name = models.CharField(max_length=20)
    series_preview = models.CharField(max_length=20, primary_key=True, unique=True)


class PhotoOfPeople(models.Model):
    name = models.CharField(max_length=20)
    human = models.ForeignKey(
        "SeriesOfPhotoShoots",
        on_delete=models.CASCADE,
    )

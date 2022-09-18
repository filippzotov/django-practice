from django.contrib import admin
from .models import Game, Genre, Company, Console, News, Comments
from .models import SeriesOfPhotoShoots, PhotoOfPeople

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Company)
admin.site.register(Console)
admin.site.register(News)
admin.site.register(Comments)

admin.site.register(SeriesOfPhotoShoots)
admin.site.register(PhotoOfPeople)
# Register your models here.

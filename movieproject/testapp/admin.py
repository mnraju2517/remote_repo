from django.contrib import admin
from testapp.models import MovieInfo

# Register your models here.
class MovieInfoAdmin(admin.ModelAdmin):
    list_display=['rdate','moviename','heroname','heroinname','rating']
    
admin.site.register(MovieInfo,MovieInfoAdmin)

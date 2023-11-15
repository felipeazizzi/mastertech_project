from django.contrib import admin
from .models import Livros

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ("titulo","autor","dispon",)
    search_field=["titulo"] 

admin.site.register(Livros,BookAdmin)

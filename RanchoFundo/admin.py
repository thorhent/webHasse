from django.contrib import admin
from .models import Clima

# Register your models here.

class ClimaAdmin(admin.ModelAdmin):
    model = Clima
    list_display = ['tempo', 'qtd', 'data']
    list_filter = ['tempo', 'qtd', 'data']
    search_fields = ['tempo', 'qtd', 'data']
    save_on_top = True


admin.site.register(Clima, ClimaAdmin)

from django.contrib import admin
from .models import Clima

# Register your models here.

class ClimaAdmin(admin.ModelAdmin):
    model = Clima
    list_display = ['qtd', 'data']
    list_filter = ['qtd', 'data']
    search_fields = ['qtd', 'data']
    save_on_top = True


admin.site.register(Clima, ClimaAdmin)
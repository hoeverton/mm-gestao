from django.contrib import admin
from .models import Foto


@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'criado_em',
    )

    search_fields = (
        'titulo',
    )

    list_filter = (
        'criado_em',
    )
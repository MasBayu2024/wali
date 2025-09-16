from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'umur', 'kota')
    search_fields = ('nama', 'kota')

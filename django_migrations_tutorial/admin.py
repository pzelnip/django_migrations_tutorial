from django.contrib import admin

from django_migrations_tutorial.models import Zapp


@admin.register(Zapp)
class ZappAdmin(admin.ModelAdmin):
    pass

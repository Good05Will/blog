from django.contrib import admin

# Register your models here.
from .models import Topic, Note

admin.site.register(Topic)
admin.site.register(Note)
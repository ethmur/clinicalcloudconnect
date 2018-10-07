from django.contrib import admin
from .models import User, HealthProvider, FilePost

admin.site.register(User)
admin.site.register(HealthProvider)
admin.site.register(FilePost)

# Register your models here.

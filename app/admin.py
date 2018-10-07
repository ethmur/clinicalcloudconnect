from django.contrib import admin
from .models import User, HealthProvider, FilePost, ProvidesFor

admin.site.register(User)
admin.site.register(HealthProvider)
admin.site.register(FilePost)
admin.site.register(ProvidesFor)

# Register your models here.

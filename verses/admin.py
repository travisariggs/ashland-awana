from django.contrib import admin

from .models import Student, Verse, Recitation

# Register your models here.
admin.site.register(Student)
admin.site.register(Verse)
admin.site.register(Recitation)

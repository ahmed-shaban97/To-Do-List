from django.contrib import admin
from .models import Task
# admin.site.register(Task)
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'complete', 'created')  # الأعمدة اللي تظهر
    list_filter = ('complete',)  # فلترة حسب الحقول
    search_fields = ('title', 'description')  # البحث حسب الحقول

admin.site.register(Task, TaskAdmin)
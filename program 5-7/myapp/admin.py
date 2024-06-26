from django.contrib import admin
from myapp.models import course, student
# Register your models here.
#admin.site.register(Student)
@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_usn','student_name','student_sem')
    ordering=('student_usn',)
    search_fields = ('student_usn',)
admin.site.register(course)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import *
from .forms import PostForm
from django.contrib.auth.models import Group

# Register your models here.

admin.site.site_header = "Dr Raju's Dashboard"

admin.site.unregister(Group)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'course', 'secondary_course', 'amount', 'paid', 'date_of_payment')
    list_filter = ('course', 'secondary_course', 'amount', 'paid', 'date_of_payment')


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'price')


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Courses, CoursesAdmin)


admin.site.register(Blog)

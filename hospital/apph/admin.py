from django.contrib import admin
from .models import Department,Doctor,Booking

# Register your models here.

admin.site.register(Department)
admin.site.register(Doctor)
class Table(admin.ModelAdmin):
    list_display = ('id','p_name','p_phone','p_email','doc_name','booking_date','booking_on')

admin.site.register(Booking,Table)
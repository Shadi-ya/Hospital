from django.urls import path
from apph import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('doctors/',views.doctors,name='doctors'),
    path('booking/',views.booking,name='booking'),
    path('contact/',views.contact,name='contact'),
    path('departments/',views.departments,name='departments'),
    path('confirmation/',views.confirmation,name='confirmation'),
]

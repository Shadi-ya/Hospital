from django.shortcuts import render,redirect
from .models import Department,Doctor
from .forms import BookingForm

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def doctors(request):
    dict_doc={
        'doctors':Doctor.objects.all()
    }
    return render(request,'doctors.html',dict_doc)
def booking(request):
    if request.method == "POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("confirmation")
    else:
        form=BookingForm()
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)
def contact(request):
    return render(request,'contact.html')
def departments(request):
    dict_dep={
        'dept':Department.objects.all()
    }
    return render(request,'departments.html',dict_dep)
def confirmation(request):
    return render(request,'confirmation.html')

from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .form import StudentForm
from .models import StudentRegistration

# Create your views here.
def registration(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = StudentRegistration(name=name,email=email,password=password)
            reg.save()
            fm = StudentForm()
    else:
        fm = StudentForm()
    student = StudentRegistration.objects.all()  
    return render(request,'enroll/add_show.html',{'form':fm,'stu':student})


def delete_stu(request,id):
    if request.method == 'POST':
        stu = StudentRegistration.objects.get(pk=id)
        stu.delete()
        return HttpResponseRedirect('/')
    
def update_stu(request,id):
    if request.method == 'POST':
        stu = StudentRegistration.objects.get(pk=id)
        fm = StudentForm(request.POST,instance=stu)
        if fm.is_valid():
            fm.save()
            return HttpResponse('Data Updated Successfully')
    else:
        stu = StudentRegistration.objects.get(pk=id)
        fm = StudentForm(instance=stu)
    return render(request,'enroll/update.html',{'form':fm})

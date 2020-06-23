from django.shortcuts import render,redirect
from Lesson3App.models import Student
from django.core.paginator import Paginator

from Lesson3App.forms import StudentForm

# Create your views here.
def list(request):
    #std=Student.objects.all()
   # std=Student.objects.order_by('email')
    std=Student.objects.all()
    paginator=Paginator(std,10)
    page=request.GET.get('page')
    students=paginator.get_page(page)
    context={'students':students,'title':'List'}
    return render(request,'list.html',context)

def create(request):
    if  request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/list/')
            except:
                pass

    else:
        form=StudentForm()
    return render(request,'create.html',{'form':form, 'title':'insert'})

def edit(request,id):
    student=Student.objects.get(pk=id)
    form=StudentForm(request.POST or None,instance=student)
    return render(request,'edit.html',{'form':form, 'title':'Edit','student':student})
        
    
from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
    "courses": Course.objects.all()
    }
    return render(request, "dart/index.html", context)

def create(request):
    name = request.POST['name']
    description = request.POST['desc']
    Course.objects.create(name = name, description = description)
    return redirect('/')

def destroy(request, id):
    context = {
    "course":Course.objects.get(id=id)
    }
    return render(request, "dart/destroy.html", context)

def delete(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/')

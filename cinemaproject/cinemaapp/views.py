from django.http import HttpResponse
from django.shortcuts import render
from.models import Category,Movie,Review
# Create your views here.
def demo(request):
    obj=Category.objects.all()
    obj1=Movie.objects.all()
    obj2=Review.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1,'result2':obj2})

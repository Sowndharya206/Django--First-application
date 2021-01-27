from django.shortcuts import render
import datetime
from django.template import loader
# Create your views here.
from django.http import HttpResponse,HttpResponseNotFound 
def mymessage(request):
     return HttpResponse("<h2>Hello, Welcome to Django!</h2>")  
#return HttpResponse("<h2>hello everyone all the best!</h3>")
def index(request):
    tim=datetime.datetime.now()
    html="<html><h4>THE TIME IS %s</h4>"%tim
    return HttpResponse(html)
def index1(request):  
    a = 1  
    if a:  
        return HttpResponseNotFound('<h1>Page not found</h1>')  
    else:  
        return HttpResponse('<h1>Page was found</h1>') # rendering the template in HttpResponse 
from django.views.decorators.http import require_http_methods
@require_http_methods(["GET"])  
def shows(request):  
     return HttpResponse('<h1>This is Http GET request.</h1>') 
def index3(request):  
    template = loader.get_template('indexes.html') # getting our template  
    name={
        'student':'rahul','course':'MCA'
        }
    return HttpResponse(template.render(name))
def img(request):  
    return render(request,'hai.html') 
def jas1(request):
    return render(request,'jas.html')  
def colo(request):
    return render(request,'color.html')  
from myapp.form import wrkForm  
def wrks(request):  
    wor = wrkForm()  
    return render(request,"button.html",{'form':wor})  
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
from myapp.form import StudentForm  
def buttons(request):  
    student = StudentForm()  
    return render(request,"button.html",{'form':student}) 
    #django validation

def wrke(request):  
    if request.method == "POST":  
        form = wrkForm(request.POST)  
        if form.is_valid():  
            try:  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = wrkForm()  
    return render(request,'button.html',{'form':form}) 
from myapp.functions.functions import handle_uploaded_file  
def image(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"button.html",{'form':student})  
import csv  
def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    writer = csv.writer(response)  
    writer.writerow(['1001', 'shiridi', 'sairam', 'CA'])  
    writer.writerow(['1002', 'padma', 'priya', 'LA', 'Testing'])   
    return response 
from myapp.models import workers      
def done(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    work = workers.objects.all()
    writer = csv.writer(response)  
    for works in work:  
        writer.writerow([works.first_name,works.last_name,works.age,works.contact])  
    return response  
from reportlab.pdfgen import canvas  
   
  
def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="sai.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello, Javatpoint. All the best")  
    p.showPage()  
    p.save()  
    return response  
def coco(request):
    return render(request,'roe.html')
from myproject import settings  
from django.core.mail import send_mail  
def mail(request):  
    subject = "Greetings"  
    msg     = "Congratulations for your success"  
    to      = "dineshkumar140498@gmail.com" 
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
    if(res == 1):  
        msg = "Mail Sent Successfuly"  
    else:  
        msg = "Mail could not send"  
    return HttpResponse(msg)  
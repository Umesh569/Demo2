from django.shortcuts import render
from .models import Contact
# Create your views here.

def index(request):
    template = "main/index.html"
    if request.method=='POST':
        # contact=Contact()
        name=request.POST.get('name')
        number=request.POST.get('number')
        email=request.POST.get('email')
        symptoms=request.POST.get('symptoms')
        severity=request.POST.get('severity')
        option=request.POST.get('option')
        date=request.POST.get('date')
        print(name,number,email,symptoms,severity,option,date) 
        contact = Contact(name=name, number=number, email=email, symptoms=symptoms, severity=severity, option=option, date=date)  
        contact.save()    
        # Contact.name=name
        # Contact.number=number
        # Contact.email=email
        # Contact.symptoms=symptoms
        # Contact.options=options
        # contact.save() 



    return render(request, template) 
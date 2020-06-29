from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from datetime import datetime
from mysite.models import About, Contact, Review, Portfolio
from django.contrib import messages
from django.core.mail import send_mail

def home(request):
    about =About.objects.all()
    revw =Review.objects.all()
    port =Portfolio.objects.all()
  
    if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            desc = request.POST.get('desc')
            home = Contact(name=name, email=email, subject=subject, desc=desc, date=datetime.today())
            home.save()
    
        #Send Mail
            send_mail(
                name +" "+ "<" + email + ">",  #name
                "Subject: " + subject + "           " + 
                "Message: " + desc, # message
                email, # from email
                ['balarsmith123@gmail.com'], # to mail
                )
        
        #return render(request, 'home.html', {})
            return HttpResponse("Thank You, Your Message has been sent!!!")

    else:
        return render(request, 'home.html',{'about':about, 'port':port, 'revw':revw}) 

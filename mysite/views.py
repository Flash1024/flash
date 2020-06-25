from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from datetime import datetime
from mysite.models import Contact, Review, Service, Portfolio
from django.contrib import messages
from django.core.mail import send_mail

def home(request):
    revw =Review.objects.all()
    serv =Service.objects.all()
    port =Portfolio.objects.all()

    if request.method == "POST":
        person_name = request.POST.get('person_name')
        jobpost = request.POST.get('jobpost')
        review = request.post.get('review')
        image = request.post.get('image')
        home = Review(person_name=person_name, jobpost=jobpost, review=review, image=image, date=datetime.today())
        home.save()

        return render(request, 'home.html',{'revw':revw})

    

    elif request.method == "POST":
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
        return render(request, 'home.html',{'serv':serv, 'port':port}) 

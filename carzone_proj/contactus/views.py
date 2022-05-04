from django.contrib import messages
from django.shortcuts import render
from .models import contactus


# Create your views here.


def contact_us(request):
    if request.method == "POST":
        full_name = request.POST['fullname']
        email = request.POST['email']
        subject = request.POST['subject']
        number = request.POST['number']
        message = request.POST['message']

        # contactus.fullname = full_name
        # contactus.email = email
        # contactus.subject = subject
        # contactus.number = number
        # contactus.message = message

        contact = contactus(fullname=full_name, email=email, subject=subject, number=number, message=message, )
        contact.save()
        print()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')

    return render(request, "pages/contact.html")

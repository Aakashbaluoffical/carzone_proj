from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Contact


# Create your views here.

def inquiry(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        user_id = request.POST['user_id']
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'you have already made an inquiry about this car. please wait until we get '
                                        'back to you.')
                return redirect('/cars/' + car_id)
        contact = Contact(car_id=car_id, first_name=first_name, last_name=last_name, customer_need=customer_need,
                          user_id=user_id, car_title=car_title,
                          city=city, state=state, email=email, phone=phone, message=message)



        contact.save()
        print()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/cars/' + car_id)

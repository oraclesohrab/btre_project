from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.


def contact(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(listing_id=listing_id,
                                                   user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'you have already made an inquery about this listing.')
                redirect('/listings/'+listing_id)

        contact = Contact(listing=listing,
                          listing_id=listing_id,
                          name=name,
                          email=email,
                          phone=phone,
                          message=message,
                          user_id=user_id,)

        contact.save()
        # Send email
        send_mail('Property listing inquiry',
                  'Hi'+name+'. \n Your inquiry on '+listing+' has been submitted',
                  'sohrabyavarzadeh@gmail.com',
                  [email],
                  fail_silently=False,)

        messages.success(
            request, 'Your inquery has been submitted, one of our realtors will contact you soon...')
        return redirect('/listings/'+listing_id)

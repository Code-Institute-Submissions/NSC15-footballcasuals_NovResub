from django.shortcuts import render, redirect, reverse
from .models import Contact


def contact_us(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        request = request.POST.get('request')

        contact.name = name
        contact.email = email
        contact.request = request
        contact.save()
        return(redirect(reverse('contact')))
    else:
        return render(request, 'contact.html')

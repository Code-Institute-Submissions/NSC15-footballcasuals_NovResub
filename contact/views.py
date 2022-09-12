from django.shortcuts import render
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
    return render(request, 'contact_us.html')

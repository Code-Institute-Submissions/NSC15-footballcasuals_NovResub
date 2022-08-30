from django.shortcuts import render, redirect


def view_bag(request):
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)

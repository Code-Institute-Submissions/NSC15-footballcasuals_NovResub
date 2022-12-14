from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ProductForm

from .models import Product, Category
# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter any search criteria!"))
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    
    return render(request, 'products/products.html', context)


@login_required()
def product_detail(request, slug):
    """A view to show the product details"""

    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


@staff_member_required()
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added!')
            return redirect(reverse('products'))
        else:
            messages.error(request,
                           ('Sorry, your product coult not be added. '
                            'Make sure the entered information is '
                            'valid.'))
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'products/add_product.html', context)


@staff_member_required()
def delete_product(request, slug):

    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted!')
        return redirect(reverse('products'))

    context = {
        'product': product,
    }

    return render(request, 'products/delete_product.html', context)

@staff_member_required()
def edit_product(request, slug):

    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product details updated')
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(request,
                           ('Sorry, product coult not be updated.'))
    else:
        form = ProductForm(instance=product)

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'products/edit_product.html', context)

def handler404(request, exception):
    return render(request, "404.html", status=404)

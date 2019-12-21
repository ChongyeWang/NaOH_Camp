from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from .forms import ProductForm
from django.http import HttpResponseRedirect


def select_language(request):
    language = 'English'
    if request.user.is_authenticated:
        if request.session.get(request.user.username, None) == None:
            request.session[request.user.username] = 'Chinese'
        language = request.session[request.user.username]

    return language


def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)

	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)

	language = select_language(request)

	return render(request,
		'product_list.html',
		{'category': category,
		'categories': categories,
		'products': products,
		'language': language})


def product_detail(request, id, slug):
	product = get_object_or_404(Product,
	                           id=id,
	                           slug=slug,
	                           available=True)

	language = select_language(request)

	cart_product_form = CartAddProductForm()

	return render(request,
	             'detail.html',
	             {'product': product,
	              'language': language,
	              'cart_product_form': cart_product_form})


def add_new_product(request):
    form = ProductForm()
    language = select_language(request)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            select = form.cleaned_data['select']
            image = form.cleaned_data['image']

            if select == "1":
            	choice = 'production'
            elif select == "2":
            	choice = 'vehicles'
            else:
            	choice = 'other'

            category = Category.objects.get(name=choice)

            product = Product(
            	category = category,
            	name = name,
            	description = description,
            	price = price,
                slug = name,
                image = image
            )
            product.save()

            return HttpResponseRedirect("/shop/")
        else:
            form = ProductForm()

    return render(request, 'add_new_product.html', {'form': form, 'language': language})

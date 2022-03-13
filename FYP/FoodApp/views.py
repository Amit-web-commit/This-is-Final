from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import CreateUserForm, ReviewForm, CartAddProductForm
from django.views.decorators.http import require_POST
from .cart import Cart
# Create your views here.
def signup(request): 
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for "+user)
            return redirect('FoodApp:loginPage')
    context={'form':form}
    return render(request, 'FoodApp/signup.html', context)

# def home(request):
#     if request.method == 'POST':
#         user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
#         if user is not None:
#             auth.login(request,user)
#             return redirect('FoodApp:home')
#         else:
#             return render (request,'FoodApp/signup.html', {'error':'Username or password is incorrect!'})
#     else:
#         return render(request,'FoodApp/signup.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('FoodApp:home')
        else:
            messages.info(request, "Username or Password is incorrect")
    context={}
    return render(request,'FoodApp/login.html',context)
def home(request):
    product = Product.objects.all()
    cart_product_form = CartAddProductForm()
    comboPackage = ComboPackage.objects.all()
    team = Team.objects.all()
    customer = CustomerProfile.objects.all()
    context = {'product':product, 'cart_product_form':cart_product_form,'comboPackage':comboPackage, 'team':team, 'customer': customer}
    return render(request, 'FoodApp/index.html', context )

def product(request):
    localProduct = LocalProduct.objects.all()
    specialProduct = SpecialProduct.objects.all()
    context = {'localProduct':localProduct, 'specialProduct':specialProduct}
    return render(request, 'FoodApp/products.html',context)

def productdetail(request, id):
    productselfs = LocalProduct.objects.filter(pk =id)
    productself = LocalProduct.objects.get(pk =id)
    comment = ReviewRating.objects.filter(product_id=id)
    context = {'productself':productself,'productselfs':productselfs,'comment':comment}
    return render(request, 'FoodApp/productdetail.html', context)

def reserveTable(request):
    context = {}
    return render(request, 'FoodApp/reservetable.html', context)

def customizeMenu(request):
    context = {}
    return render(request, 'FoodApp/customizemenu.html', context)


def editIngredients(request):
    context= {}
    return render(request, 'FoodApp/edit.html', context)

def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email  = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('msg')
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.message = message
        contact.save()
        return redirect ('/')
    return render(request, 'FoodApp/contact.html')

def carttotal(request):
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     items = order.orderitem_set.all()
    # else:
    #     items = []

    context={}
    return render(request,'FoodApp/carttotal.html', context)

def submit_review(request, id):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        form  = ReviewForm(request.POST)
        if form.is_valid():
            data = ReviewRating()
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.review = form.cleaned_data['review']
            data.product_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(request, "Thanks,Review has been submitted")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


# def submit_review(request, id):
#     url = request.META.get("HTTP_REFERER")
#     if request.method == "POST":
#         try:
#             reviews = ReviewRating.objects.get(user_id=request.user.id, product_id =id)
#             form = ReviewForm(request.POST, instance = reviews)
#             form.save()
#             messages.success(request, "Thanks, Review has been updated")
#             return  render(url)


#         except ReviewRating.DoesNotExist:
#             form = ReviewForm(request.POST)
#             if form.is_valid():
#                 data = ReviewRating()
#                 data.comment = form.cleaned_data['comment']
#                 data.rating = form.cleaned_data['rate']
#                 data.review = form.cleaned_data['review']
#                 data.product_id = id
#                 data.user_id = request.user.id
#                 data.save()
#                 messages.success(request, "Thanks, Review has been submitted")
#                 return redirect(url)

# def submit_review(request,id):
            
#     if request.method == "GET":
#         review = ReviewRating()
        
#         prod_id = request.GET.get('prod_id')
#         product = LocalProduct.objects.get(id = prod_id)
#         comment = request.GET.get('comment')
#         rev = request.GET.get('review')
#         rate = request.GET.get('rate')
#         user = request.user
#         review.prod_id = prod_id
#         review.product = product
#         review.comment = comment
#         review.subject = rev
#         review.rate = rate
#         review.user=user
#         review.save()
#         return redirect('FoodApp:home', id=prod_id)
    # product = get_object_or_404(LocalProduct, pk=id)
    # pro = LocalProduct.objects.get(id=id)
    # if request.method == "POST":
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         product = form.cleaned_data['product']
    #         user = form.cleaned_data['user']
    #         review = form.cleaned_data['review']
    #         comment = form.cleaned_data['comment']
    #         rate = form.cleaned_data['rate']

    #         product = request.POST.get('product', ''),
    #         user = request.POST.get('user', ''),
    #         review = request.POST.get('review', ''),
    #         comment = request.POST.get('comment', ''),
    #         rate = request.POST.get('rate', ''),
    #         obj = ReviewRating (product=product, user=user, review=review, comment=comment, rate=rate)
    #         obj.save()
    #         context = {'obj': obj}
    #         return render(request, 'FoodApp/productdetail.html',context)
    #     else:
    #         form = ReviewForm()
    #     return HttpResponse('Please rate the product') 
@require_POST
def cart_add(request, id):
    
    cart = Cart(request)
    product = get_object_or_404(Product, id = id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product = product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('FoodApp:carttotal')

def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect('FoodApp:carttotal')

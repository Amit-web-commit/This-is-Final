from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, JsonResponse
import json
from django.contrib import messages
from .models import *
from .forms import CreateUserForm, ReviewForm, CartAddProductForm, ReserveTableForm
from django.views.decorators.http import require_POST
from .cart import Cart
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .utils import cookieCart
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
def logoutPage(request):
    logout(request)
    return redirect("FoodApp:loginPage")
def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create()
        items = order.orderitem_set.all()
    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     data = LocalProduct.objects.filter(name__icontains=q)
    # else:

    product = LocalProduct.objects.filter(productType= "EditProduct")
    cart_product_form = CartAddProductForm()
    comboPackage =  LocalProduct.objects.filter(productType="ComboPackage")
    team = Team.objects.all()
    customer = CustomerProfile.objects.all()
    context = {'product':product, 'cart_product_form':cart_product_form,'comboPackage':comboPackage, 'team':team, 'customer': customer}
    return render(request, 'FoodApp/index.html', context )

def product(request):
    
    if 'q' in request.GET:
        q = request.GET['q']
        # localProduct = LocalProduct.objects.filter(name__icontains=q)
        # specialProduct = LocalProduct.objects.filter(name__icontains=q)
        # multiple_q = Q(Q(name__icontains=q) | Q(name__icontains=q))
        # localProduct = LocalProduct.objects.filter(multiple_q)

        localProduct = LocalProduct.objects.filter(name__icontains=q)
        specialProduct = LocalProduct.objects.filter(name__icontains=q)
    else:
        localProduct = LocalProduct.objects.filter(productType=1)
        specialProduct = LocalProduct.objects.filter(productType="SpecialProduct")
        specialProducts = LocalProduct.objects.filter(productType="SpecialProduct").order_by("id")
    # p = Paginator(specialProducts,3)
    # print("Pages:", p.num_pages)
    # page_number = request.GET.get('page')
    # product_list = Paginator.get_page(p,page_number)
    context = {'localProduct':localProduct, 'specialProduct':specialProduct}
    return render(request, 'FoodApp/products.html',context)

def productdetail(request, id):
    productselfs = LocalProduct.objects.filter(pk =id)
    productself = LocalProduct.objects.get(pk =id)
    comment = ReviewRating.objects.filter(product_id=id)
    context = {'productself':productself,'productselfs':productselfs,'comment':comment}
    return render(request, 'FoodApp/productdetail.html', context)

def reserveTable(request):
    form = ReserveTableForm()
    # if request.user.is_authenticated:
    #     customer = request.user
    #     order,created = Order.objects.get_or_create()
    #     items = order.orderitem_set.all()
    if request.method == 'POST':
        
        form  = ReserveTableForm(request.POST)
        # if form.is_valid():
        form = ReserveTable()
        tableNo =request.POST.get('tableNo') 
        date = request.POST.get('date') 
        hours = request.POST.get('selecthour') 
        name = request.POST.get('name') 
        email =request.POST.get('email')
        person =request.POST.get('person') 
        current_user = request.user
    
        form = ReserveTable( tableNo=tableNo, date=date, selecthour=hours, name=name, email=email, person=person)
        form.save()
        
        messages.success(request, "Thanks,Your Requested table is booked.")

    context = {'form':form}
    return render(request, 'FoodApp/reservetable.html', context)
@login_required(login_url='FoodApp:loginPage')
def customizeMenu(request):
    if request.method == "POST":
        
        customizemenu = CustomizeMenu()
        yourName = request.POST.get('yourName')
        yourEmail = request.POST.get('yourEmail')
        role = request.POST.get('role')
        yourCuisine = request.POST.get('yourCuisine')
        Ingredients1 = request.POST.get('Ingredients1')
        Ingredients2 = request.POST.get('Ingredients2')
        Ingredients3 = request.POST.get('Ingredients3')
        recipedetail = request.POST.get('recipedetail')
        customizemenu  = CustomizeMenu(customerName=yourName, customerEmail=yourEmail, cusineType=role, cusineName=yourCuisine, 
        ingridents1=Ingredients1, ingridents2=Ingredients2, ingridents3=Ingredients3, recipeDetail=recipedetail)
        customizemenu.save()
        messages.success(request, "Thanks,The Suggessted Cusine is recorded.")
        return redirect('FoodApp:customizemenu')
    
    return render(request, 'FoodApp/customizemenu.html')


def editIngredients(request):
    context= {}
    return render(request, 'FoodApp/edit.html', context)

def contact(request):
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create()
        items = order.orderitem_set.all()
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
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create()
        items = order.orderitem_set.all()
        cartItems = order.get_itemtotal

    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
 

    context={'items':items, 'order':order, 'cartItems':cartItems}
   
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

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('productId:', productId)
    customer = request.user
    localProduct = LocalProduct.objects.get(id=productId)
    
    order,created = Order.objects.get_or_create()
    orderItem, created = OrderItem.objects.get_or_create(order=order, localProduct=localProduct)

    if action == "add":
        orderItem.quantity +=1
        orderItem.save()
    

    
    return JsonResponse("Item is added", safe=False)

def updateQuantity(request):
    data = json.loads(request.body)
    quantityFieldValue = data['qfv']
    quantityFieldProducts = data['qfp']
    product = OrderItem.objects.filter(localProduct__name = quantityFieldProducts).last()
    product.quantity = quantityFieldValue
    product.save()
    return JsonResponse("Updated", safe=False)

def payment(request):
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user
        order,created = Order.objects.get_or_create()
        total = float(data['cart_total'])

        if total ==order.convertDollar:
            
            order.save()
    
            order = {'get_cart_total':0, 'get_itemtotal':0, 'get_local_total':0}
    
            
    return JsonResponse("It is Working", safe=False)
    # context= {}
    # return render(request,'FoodApp/payment.html', context)

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
# @require_POST
# def cart_add(request, id):
    
#     cart = Cart(request)
#     product = get_object_or_404(Product, id = id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product = product, quantity=cd['quantity'], override_quantity=cd['override'])
#     return redirect('FoodApp:carttotal')

# def cart_remove(request, id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=id)
#     cart.remove(product)
#     return redirect('FoodApp:carttotal')



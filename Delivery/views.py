#from .Pedi2.settings import TIME_ZONE
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm
from django.contrib.auth import login, authenticate, logout
from .models import Restaurant, Product
from .shoppingCart import ShoppingCart

#############################User Log#################################

#Register
def registerPage(request):

    #Creating Form
    form = CreateUserForm()

    #input user data in the form
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        #Checking user data, if is valid save
        if form.is_valid():
            form.save()
            return redirect('delivery:login')
    
    #else:
    #    redirect('delivery:index')
    context = {
        "form": form,
    }
    return render(request, "login/register.html", context)



#Login
def loginPage(request):
    
    #input user data in the form
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #authenticate user data
        user = authenticate(request, username=username, password=password)

        #if user data is OK, then log user and redirect to Index
        if user is not None:
            login(request, user)
            return redirect('delivery:index')
            
    return render(request, "login/login.html")

#Logout
def logoutUser(request):
    logout(request)
    return redirect('delivery:login')

#############################DeliveryApp############################
def home(request):
    return render(request, "home/home.html")

#Delivery index full of restaurants
def index(request):
    
    #redirect to login if user not log
    if not request.user.is_authenticated:
        return redirect('delivery:login')
    
    #getting log user and all restaurants
    user = request.user
    restaurants = Restaurant.objects.all()

    #context for using in the frontend
    context = {
        'restaurants': restaurants,
        'user':user,
    }

    return render(request, "Delivery/index.html", context)



#Restaurant
def restaurant(request, restaurant_id):

    #same as index if user not login, then redirect to login page
    if not request.user.is_authenticated:
        return redirect('delivery:login')

    #get user
    user = request.user

    #if not restaurant 404
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    
    #getting all the products
    products = Product.objects.filter(restaurant_id=restaurant_id)
    context = {
        'products': products,
        'user':user,
        'restaurant': restaurant
    }
    return render(request, "Restaurant/restaurant.html", context)


def checkout(request):
    return render(request, "checkout/checkout.html")

########################ShoppingCart################################

#Add product by id
def addProduct(request, id):

    #using shopping cart model
    cart = ShoppingCart(request)

    #getting the product by de id
    product = Product.objects.get(id=id)

    #adding 1 product with the id requested
    cart.add(product=product)

    #refresh page
    return redirect(request.META['HTTP_REFERER'])

#Delete product by id
def deleteProduct(request, id):

    #using shopping cart model
    cart = ShoppingCart(request)
    
    #getting the product by de id
    product = Product.objects.get(id=id)

    #delete the product with id requested
    cart.deleteProduct(product=product)

    #refresh page
    return redirect(request.META['HTTP_REFERER'])

#Substract 1 product by id
def substractProduct(request, id):

    #using shopping cart model
    cart = ShoppingCart(request)

    #getting the product by de id
    product = Product.objects.get(id=id)

    #product quantity -1 
    cart.substractProduct(product=product)

    #refresh page
    return redirect(request.META['HTTP_REFERER'])

def cleanCart(request):

    #using shopping cart model
    cart = ShoppingCart(request)

    #deleting all products    
    cart.cleanCart()

    #refresh page
    return redirect(request.META['HTTP_REFERER'])

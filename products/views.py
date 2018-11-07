from django.shortcuts import render, redirect
from .models import Product
import datetime

# Create your views here.
def index(request):
    return render(request, "products/index.html")

def create(request):

    if request.method == "POST":
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
            product = Product()
            product.title = request.POST['title']
            product.pub_date = datetime.datetime.now()
            product.body = request.POST['body']
            if request.POST['url'].startswith("http://") or request.POST['url'].startswith("https://"):
                product.url = request.POST['url']
            else:
                product.url = "http://" + request.POST['url']
            product.image = request.FILES['image']
            product.icon = request.FILES['icon']
            product.hunter = request.user
            product.save()
            return redirect("home")
        else:
            return render(request, "products/create.html", {"error":"All Fields Are Required."})
    else:
        return render(request, "products/create.html")
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "products/index.html", {"products":products})

@login_required
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
            return redirect("detail", product_id=int(product.id))
        else:
            return render(request, "products/create.html", {"error":"All Fields Are Required."})
    else:
        return render(request, "products/create.html")

@login_required
def detail(request, product_id):

    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect("detail", product_id=product.id)
    else:
        product = get_object_or_404(Product, pk=product_id)
        return render(request, "products/detail.html", {"product":product})
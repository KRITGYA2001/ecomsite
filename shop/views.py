from django.shortcuts import render
from .models import Products,Order
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    product_objects=Products.objects.all()
    
    #search code
    item_name=request.GET.get('item_name')
    if item_name!='' and item_name is not None:
        product_objects=product_objects.filter(title__icontains=item_name)
    
    #paginator code
    paginator = Paginator(product_objects,8)
    page=request.GET.get('page')
    product_objects= paginator.get_page(page)
    
    return render(request,'shop/index.html',{'product_objects':product_objects})

@login_required
def detail(request,id):
    product_object = Products.objects.get(id=id)
    
    return render(request,'shop/detail.html',{'product_object':product_object})


@login_required
def checkout(request):
    if request.method == "POST":
        items=request.POST.get("items",'')
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        address = request.POST.get("address","")
        city= request.POST.get("city","")
        state = request.POST.get("state","")
        zipcode = request.POST.get("zipcode","")
        total = request.POST.get("total","")
        
        order=Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
        order.save()
    return render(request,'shop/checkout.html')
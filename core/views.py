from django.shortcuts import render,redirect,get_object_or_404
from core.models import *

# Create your views here.
def homepage(req):
    card = Product.objects.all()
    return render(req, "homepage.html",{"card":card})


def addtocart(req,product_id):
    product = get_object_or_404(Product,id=product_id)
    
    cart = req.session.get('cart',[])
    
    for item in cart:
        if item['id']==product.id:
            item['qty']+=1  
            req.session['cart'] = cart
            return redirect("homepage")
        
    cart.append({
        'id': product.id,
        'name': product.name,
        'image': product.image.url,  # Get the image URL
        'description': product.description,
        'price': product.price,
        'qty':1,
    })
    req.session['cart'] = cart
    return redirect("homepage")

def viewcart(req):
    cart = req.session.get('cart',[])
    totalprice=sum(item['price']*item['qty']for item in cart)
    print(totalprice)
    taxprice = round(totalprice*0.18,2)
    finalprice = totalprice+taxprice
    print(finalprice)
    return render(req, "cart.html", {"cart":cart,'totalprice':totalprice,'taxprice':taxprice,'finalprice':finalprice})

def clear(req,product_id):
        cart = req.session.get('cart',[])
        cart = [item for item in cart if item['id'] !=product_id]
        req.session['cart']=cart
        return redirect("viewcart")

def cartclear(req,action):
    if action == 'ac':
        req.session['cart']=[]
        return redirect('viewcart')
    else:
        return redirect('viewcart')
    return redirect("viewcart")

def updateqty(req, action, product_id):
    cart = req.session.get('cart',[])
    for items in cart:
        if items['id']==int(product_id):
            if action == 'inc':
                items['qty']+=1
            elif action=='dec'and items['qty'] > 1:
                items['qty']-=1
            break
    req.session['cart']=cart
    return redirect("viewcart")


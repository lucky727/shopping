from django.shortcuts import render,redirect,get_object_or_404
from core.models import *
import razorpay
from django.conf import settings



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




def initiate_payment(request,amount):
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    order_amount = amount*100 # Amount in paisa (₹500.00)
    order_currency = 'INR'
    
    # 🔹 Razorpay Order Create Karna
    payment_order = client.order.create({
        'amount': order_amount,
        'currency': order_currency,
        'payment_capture': '1'
    })

    # 🔹 Order ID Session Me Store Karna
    request.session['order_id'] = payment_order['id']

    return render(request, 'payment.html', {
        'api_key': settings.RAZORPAY_KEY_ID,
        'order_id': payment_order['id'],
        'amount': order_amount // 100  # Convert to Rupees
    })



from django.http import HttpResponse

def payment_success(request):
    return render(request,"payments_success.html")


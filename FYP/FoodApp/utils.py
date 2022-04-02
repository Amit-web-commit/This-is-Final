from .models import *
import json

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['Cart'])
    except:
        cart={}
    print('Cart: ', cart)
    items = []
    order = {'get_cart_total':0, 'get_itemtotal':0, 'get_local_total':0}
    cartItems = order ['get_itemtotal']
        
    for i in cart:
        try:
            cartItems += cart[i]["quantity"]

            localProduct = LocalProduct.objects.get(id=i)
            total = (localProduct.price * cart[i]["quantity"])
            localtotal = localProduct.price * cart[i]["quantity"]
            # quantity=orderItem.quantity
            order['get_cart_total'] += total

            order['vat'] = order['get_cart_total'] *0.05
            order['grant_total']= order['get_cart_total'] + order['vat']
            order['get_itemtotal'] += cart[i]["quantity"]
            
            
            # print(localtotal)
            # print(localtotal)
            item = {
                'localProduct':{
                    'id':localProduct.id,
                    'name': localProduct.name,
                    'price': localProduct.price,
                    # 'quantity':OrderItem.quantity,
                    'localProductimage': localProduct.localProductimage,
                },
                'quantity': cart[i]["quantity"],
                'get_cart_total': total,
                'vat': order ,
                'grant_total':total,
                'get_local_total':localtotal,     
            }
            items.append(item)
        except:
            pass
    return {'cartItems':cartItems, 'order':order, 'items':items}
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from shopapp.models import *
from . models import *

# Create your views here.

def cart(request,tot=0,count=0,cartitem=None,tax=0.05,shipping=15):

    try:
        ct=cartlist.objects.get(cartid=cartidd(request))
        citem=item.objects.filter(cart=ct,active=True)
        for i in citem:
            tot +=(i.prd.price*i.qlt)
            count+=i.qlt
        tax = tot * tax
        if tot > 0:
            total = tot + tax + shipping
        else:
            total = 0
    except ObjectDoesNotExist:
        pass

    return render(request,'carts.html',{'ci':citem,'t':tot,'cd':count,'tax':tax,'total':total})
def cartidd(request):
    cid=request.session.session_key
    if not cid:
        cid=request.session_create()
    return cid
def addcart(request,prdid):
    proud=product.objects.get(id=prdid)
    try:
        ct=cartlist.objects.get(cartid=cartidd(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cartid=cartidd(request))
        ct.save()
    try:
        ctitem=item.objects.get(prd=proud,cart=ct)
        if ctitem.qlt < ctitem.prd.stock:
            ctitem.qlt+=1
        ctitem.save()
    except item.DoesNotExist:
        ctitem=item.objects.create(prd=proud,qlt=1,cart=ct)
        ctitem.save()
    return redirect('details')



def minus(request,prdid):
    ct=cartlist.objects.get(cartid=cartidd(request))
    prod=get_object_or_404(product,id=prdid)
    citem=item.objects.get(prd=prod,cart=ct)
    if citem.qlt>1:
        citem.qlt-=1
        citem.save()
    else:
        citem.delete()
    return redirect('details')
def delete(requst,prdid):
    ct = cartlist.objects.get(cartid=cartidd(requst))
    prod = get_object_or_404(product, id=prdid)
    citem = item.objects.get(prd=prod, cart=ct)
    citem.delete()
    return redirect('details')



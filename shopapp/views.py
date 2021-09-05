from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from . models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def home(requst,slugs=None):
        cpage=None
        prd=None
        if slugs!=None:
            cpage=get_object_or_404(catag,slug=slugs)
            prd=product.objects.filter(cata=cpage,available=True)
        else:
            prd = product.objects.all().filter(available=True)
        cat=catag.objects.all()
        paginator=Paginator(prd,6)
        try:
            page=int(requst.GET.get('page',1))
        except:
            page=1
        try:
            pro=paginator.page(page)
        except(EmptyPage,InvalidPage):
            pro=paginator.page(paginator.num_pages)
        return render(requst,'index.html',{'prd':prd,'cat':cat,'pg':pro})
def prddetails(requst,slugs,prdslug):
    try:
        prod=product.objects.get(cata__slug=slugs,slug=prdslug)
    except Exception as e:
        raise e


    return render(requst,'item.html',{'pr':prod})
def search(requst):
    prod=None
    qury=None
    if 'q' in requst.GET:
        qury=requst.GET.get('q')
        prod=product.objects.all().filter(Q(name__contains=qury)|Q(des__contains=qury))
    return render(requst,'sh.html',{'qr':qury,'pr':prod})





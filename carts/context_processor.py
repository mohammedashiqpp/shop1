
from . views import  *
def count(request):
    itemcount=0;
    if 'admin' in request.path:
        return {}
    else:
        try:

           ct=cartlist.objects.filter(cartid=cartidd(request))
           cti=item.objects.all().filter(cart=ct[:1])
           for c in cti:
               itemcount+=c.qlt
        except cartlist.DoesNotExist:
            itemcount=0
        return dict(its=itemcount)

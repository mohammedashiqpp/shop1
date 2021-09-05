from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.
class catag(models.Model):
    name=models.CharField(max_length=225,unique=True)
    slug=models.SlugField(max_length=225,unique=True)
    class Meta:
        ordering=('name',)
        verbose_name='cata'
        verbose_name_plural='catagory'
    def get_url(self):
        return reverse('dview',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class product(models.Model):
    name=models.CharField(max_length=225,unique=True)
    slug=models.SlugField(max_length=225,unique=True)
    img=models.ImageField(upload_to='product')
    des=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    cata=models.ForeignKey(catag,on_delete=models.CASCADE)
    def get_url(self):
        return  reverse('detail',args=[self.cata,self.slug])
    def __str__(self):
        return '{}'.format(self.name)


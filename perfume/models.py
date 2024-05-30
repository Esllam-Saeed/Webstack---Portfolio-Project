from django.db import models
import datetime
# Create your models here.
class Perfume(models.Model):
    #name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='uploads/product/')
    stock = models.IntegerField()
    is_sale = models.BooleanField(default=False)
    sale_price =models.FloatField(default=0)

    def __str__(self) :
        return self.brand
                                
class customer (models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    password =models.CharField(max_length=100)
    
class orders (models.Model):
    product =models.ForeignKey(Perfume,on_delete=models.CASCADE)
    customer= models.ForeignKey(customer,on_delete=models.CASCADE)
    quantity =models.IntegerField(default=1)
    address= models.CharField(max_length=100, default='',blank=True)
    phone =models.CharField(max_length=20,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)
    def __str__(self) :
        return self.product
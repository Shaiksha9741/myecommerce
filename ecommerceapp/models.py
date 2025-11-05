from django.db import models

# Create your models here.
class Contact(models.Model):
    #contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    desc=models.TextField(max_length=200)
    phonenumber=models.IntegerField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50, default="")
    subcategory=models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desc=models.TextField(max_length=200, default="")
    # pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images")

    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    order_id =models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=90)
    email=models.EmailField(max_length=90)
    address1=models.CharField(max_length=50)
    address2=models.CharField(max_length=50, default="")
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.CharField(max_length=50)
    oid=models.CharField(max_length=150, blank=True)
    amountpaid=models.IntegerField( blank=True, null=True)
    paymentstatus= models.CharField(max_length=500, blank=True, null=True)
    phone=models.CharField(max_length=50, default="")


    def __str__(self):
        return self.name
    
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=500)
    delivered = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..." + self.update_desc[-7:]

   
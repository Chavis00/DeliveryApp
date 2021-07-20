from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import TextChoices
from django.utils import timezone

#Customer
class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True, null=True)
    
    def DeliveryTime(self):
        pass

#Restaurant
class Restaurant(models.Model):

    name = models.TextField(verbose_name='Restaurant Name', max_length= 20)
    desc = models.TextField(verbose_name='Description', max_length= 50, blank=True)
    food = models.TextField(verbose_name='Food', max_length=30, blank=True)
    pic = models.ImageField(null=True)
    category = models.TextField(null=True, blank=True)
    open = models.TimeField(null=True)
    close = models.TimeField(null=True)
    status = models.BooleanField(null=True, default=0)
   
    #Shows if is Open or Close
    def OpenClose(self):

        now = timezone.now()
        now = now.time()   

        if ((now.hour > self.open.hour) and (now.hour < self.close.hour)) or ((now.hour == self.open.hour and now.minute > self.open.minute and now.minute < self.close.minute)):
            self.status = 1
            return "Open"

        self.status = 0
        return "Close"
    
    #If is Close shows the start time
    def OpensAt(self):
        return "Opens at " + str("{:02d}".format(int(self.open.hour)))+":" + str("{:02d}".format(int(self.open.minute)))
        
    def __str__(self):
        return self.name



#Product
class Product(models.Model):

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default="")
    name = models.TextField(verbose_name='Product Name', max_length=40)
    price = models.DecimalField(verbose_name='$', max_digits=6, decimal_places=2)
    pic = models.ImageField(null=True, blank=True)
    desc = models.TextField(verbose_name="Description", max_length=200)
 
    def __str__(self):
        return self.name



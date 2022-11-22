from django.db import models
from account.models import CustomeUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Collection(models.Model):
    collection = models.CharField(_('Collection'),max_length=200)
    pdf = models.FileField()

    def __str__(self):
        return f"{self.collection}"


class Thickness(models.Model):
    thickness = models.CharField(_('Thickness'),max_length=200)

    def __str__(self):
        return f"{self.thickness}"

class Size(models.Model):
    size = models.CharField(_('Size'),max_length=200)

    def __str__(self):
        return f"{self.size}"

class Surface(models.Model):
    surface = models.CharField(_('Surface'),max_length=200)

    def __str__(self):
        return f"{self.surface}"

class Product(models.Model):
    product_name = models.CharField(_('Product Name'),max_length=200,null=True)
    collection = models.ForeignKey(Collection,on_delete=models.CASCADE)
    surface = models.ForeignKey(Surface,on_delete=models.CASCADE)
    weight = models.CharField(_('Weight'),max_length=200)
    thickness = models.ForeignKey(Thickness,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    product_image = models.ImageField(_('Product Image'))
    preview = models.ImageField(_('Preview'),max_length=30)
    is_deleted = models.BooleanField(_('Is Delete'),default = False)
    product_quantity = models.IntegerField(_('Product Quantity'),default=0)

    def __str__(self):
        return f"{self.product_name}|{self.collection}"


class OrderGeneration(models.Model):
    user_id = models.ForeignKey(CustomeUser,on_delete=models.CASCADE)
    order_date = models.DateTimeField(_('order Date'))
    order_time = models.TimeField(_('Order Time'))
    order_total_weight = models.DecimalField(_('Order Total Weight'),max_digits=10, decimal_places=2)
    order_total_box = models.IntegerField(_('Order Total Box'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_ind = models.IntegerField(_('Price Individual piece'),default=0)
    total_price = models.DecimalField(_('Total Price'),max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(_('Is Deleted'),default = False)

    def __str__(self):
        return f"{self.user_id} | {self.product} | {self.total_price}"

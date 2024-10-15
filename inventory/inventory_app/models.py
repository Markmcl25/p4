from django.db import models

# Create your models here.
class Item(models.Model):  
    # Define your fields here
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    stock = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# To group items into categories.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# To track orders and item transactions.
class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} for {self.item.name}"

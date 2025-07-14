from django.db import models

from .validators import positive_value, bolivian_phone_number


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Candy(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[positive_value])
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='candys')

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100, validators=[bolivian_phone_number])
    address = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}. {self.customer.first_name} {self.customer.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    candy = models.ForeignKey(Candy, on_delete=models.CASCADE, related_name='candy')
    quantity = models.IntegerField(validators=[positive_value])
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[positive_value])

    def __str__(self):
        return f"{self.id}. {self.order.customer.first_name} {self.order.customer.last_name}"

    def get_total(self):
        return self.price * self.quantity

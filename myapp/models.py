# from django.db import models


# class User(models.Model):
#     username = models.CharField(max_length=25,unique=True)


# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     amount = models.DecimalField(decimal_places=2,max_digits=5)

# class PurchaseOrder(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     Product = models.ForeignKey(Product,on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()


# user1 = User.objects.create(username='user 1')
# user2 = User.objects.create(username='user 2')
# user3 = User.objects.create(username='user 3')

# product_a = Product.objects.create(name='product a', amount=100)
# product_b = Product.objects.create(name='product b', amount=120)
# product_c = Product.objects.create(name='product c', amount=150)

# PurchaseOrder.objects.create(user=user1,product=product_a,quantity=3)
# PurchaseOrder.objects.create(user=user2,product=product_b,quantity=5)
# PurchaseOrder.objects.create(user=user3,product=product_c,quantity=5)
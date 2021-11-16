# from django.db import models
# from django.db.models import CASCADE
#
# from main.models.base import BaseModel
# from main.models.item import Item
# from main.models.user import User
#
#
# class Status(BaseModel):
#     code = models.IntegerField()
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return str(self.code)
#
#     class Meta:
#         db_table = "status"
#         verbose_name = "Status"
#         verbose_name_plural = "Statuses"
#
#
# class Basket(BaseModel):
#     name = models.CharField(max_length=32)
#     owner = models.ForeignKey(User, on_delete=CASCADE, related_name="baskets")
#     delivery_address = models.CharField(null=True, blank=True, max_length=500)
#     status = models.ForeignKey(
#         Status,
#         on_delete=models.CASCADE,
#         related_name="baskets")
#     favourite = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = "basket"
#
#
# class Order(BaseModel):
#     basket = models.ForeignKey(Basket, on_delete=CASCADE, related_name="basket_items")
#     item = models.ForeignKey(Item, on_delete=CASCADE, related_name="orders")
#     required_amount = models.IntegerField()
#
#     def __str__(self):
#         return f"Order № {self.pk}"
#
#     class Meta:
#         db_table = 'basket_item'

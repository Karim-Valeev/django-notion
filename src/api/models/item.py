# from django.db import models
# from django.db.models import CASCADE
#
# from main.models.base import BaseModel
# from main.models.item_tags import Shop, Category
# from main.models.user import User
#
#
# class Item(BaseModel):
#     name = models.CharField(max_length=256)
#     # Тк цена обычно 399,99$
#     price = models.DecimalField(max_digits=1000, decimal_places=2)
#     shop = models.ForeignKey(Shop, on_delete=CASCADE, related_name="items")
#     category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name="category_items")
#
#     icon = models.ImageField(null=True, blank=True)
#
#     amount = models.IntegerField()
#
#     kcal = models.IntegerField(null=True, blank=True)
#     proteins = models.IntegerField(null=True, blank=True)
#     fats = models.IntegerField(null=True, blank=True)
#     carbohydrates = models.IntegerField(null=True, blank=True)
#     like_counter = models.IntegerField(default=0)
#
#     def __str__(self):
#         return f"{self.name}, {self.shop.__str__()}"
#
#     class Meta:
#         db_table = "item"
#
#
# class ItemComment(BaseModel):
#     item = models.ForeignKey(Item, on_delete=CASCADE, related_name='comments')
#     owner = models.ForeignKey(User, related_name='user_comments', on_delete=CASCADE)
#     text = models.TextField()
#
#     def __str__(self):
#         return f"Comment: {self.item.name}, {self.owner.username}, {self.created_at}"
#
#     class Meta:
#         db_table = "item_comment"
#
#
# class ItemLike(BaseModel):
#     item = models.ForeignKey(Item, on_delete=CASCADE)
#     owner = models.ForeignKey(User, on_delete=CASCADE)
#
#     def __str__(self):
#         return f"{self.item.__str__()}, {self.owner.username}"
#
#     class Meta:
#         db_table = "item_like"
#
#
# class PurchaseHistory(models.Model):
#     user = models.ForeignKey(User, on_delete=CASCADE, related_name="purchases")
#     item = models.ForeignKey(Item, on_delete=CASCADE, related_name="purchases")
#     amount_purchased = models.IntegerField()
#     item_price_at_the_moment = models.DecimalField(max_digits=1000, decimal_places=2)
#     sale_at_the_moment = models.DecimalField(default=0.0, max_digits=3, decimal_places=2)
#     date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Purchase [{self.pk}]"
#
#     class Meta:
#         db_table = "purchase_history"
#         verbose_name = "Purchase history"
#         verbose_name_plural = "Purchase history"

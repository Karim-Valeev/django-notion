# from django.db import models
# from django.db.models import CASCADE
#
# from main.models.item import Item
#
#
# class Sale(models.Model):
#     item = models.ForeignKey(
#         Item,
#         on_delete=CASCADE,
#         related_name="sales"
#     )
#     value = models.DecimalField(default=0.0, max_digits=3, decimal_places=2)
#     from_date = models.DateTimeField()
#     to_date = models.DateTimeField()
#
#     def __str__(self):
#         return f"Sale [{self.pk}]"
#
#     class Meta:
#         db_table = "sale"
#         verbose_name = "Sale"
#         verbose_name_plural = "Sales"

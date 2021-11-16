# from django.db import models
#
# from main.models.base import BaseModel
#
#
# class Shop(BaseModel):
#     site = models.URLField()
#     name = models.CharField(max_length=32)
#     address = models.CharField(max_length=500)
#
#     def __str__(self):
#         return f"{self.name}, address: {self.address}"
#
#     class Meta:
#         db_table = "shop"
#
#
# class Category(BaseModel):
#     name = models.CharField(max_length=100)
#     description = models.TextField(null=True, blank=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = "category"
#         verbose_name = "Category"
#         verbose_name_plural = "Categories"

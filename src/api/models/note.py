from django.db import models

from .base import BaseModel
from .user import User


class Note(BaseModel):
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, verbose_name="Author")
    # У URLField как будто где-то дефолтное значени "" стоит
    url = models.URLField(max_length=500, null=False, blank=False, verbose_name="URL")
    topic = models.CharField(max_length=500, null=False, blank=False, verbose_name="Topic")
    body = models.TextField(null=True, blank=True, verbose_name="Body")
    parent = models.ForeignKey(
        "Note", null=True, blank=True, on_delete=models.CASCADE, related_name="notes", verbose_name="Parent node"
    )

    def __str__(self):
        return self.topic

    class Meta:
        db_table = "note"
        verbose_name = "Note"
        verbose_name_plural = "Notes"

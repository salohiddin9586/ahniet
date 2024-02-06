from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    title = models.CharField(
        max_length=50,
        verbose_name="nazvanie")
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
        verbose_name="kategori"
    )

    def __str__(self):
        return self.title
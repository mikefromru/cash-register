from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.title} {self.price}'
    
    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'

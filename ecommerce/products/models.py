from django.db import models

# Create your models here.

from django.db import models

class Kategoriya(models.Model):
    category_name = models.CharField(max_length=35)
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriya"
    


class Mahsulotlar(models.Model):
    category = models.ForeignKey(Kategoriya, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    oldprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, help_text="Bo'sh qolishi mumkin", default=0)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Bo'sh qolishi mumkin", default=0)

    def save(self, *args, **kwargs):
        if self.oldprice is not None and self.price is not None:
            discount_percentage = ((self.oldprice - self.price) / self.oldprice) * 100
            self.discount = discount_percentage
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

    @property
    def discount_sign(self):
        if self.discount is not None:
            return "+" if self.discount > 0 else "-" if self.discount < 0 else ""
        return ""

    class Meta:
        verbose_name = "Mahsulotlar"
        verbose_name_plural = "Mahsulotlar"

class Mahsulot_rasm(models.Model):
    product = models.ForeignKey(Mahsulotlar, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"
    
    class Meta:
        verbose_name = "Mahsulot_rasm"
        verbose_name_plural = "Mahsulot_rasm"
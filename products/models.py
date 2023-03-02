from django.db import models


# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категорія Товарів'
        verbose_name_plural = 'Категорія Товарів'


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description_short = models.TextField(max_length=75, blank=True, null=True, default=None)
    description = models.TextField(max_length=1024, blank=True, null=True, default=None)
    weight_item = models.TextField(max_length=24, blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    popular = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        if self.discount == 0:
            return f'{self.id}: {self.name}, {self.price}'
        else:
            return f'{self.id}: {self.name}, {self.discount_price}'


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def save(self, *args, **kwargs):
        self.discount_price = round(self.price - ((self.price * self.discount) / 100))

        super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Зображення продукту'
        verbose_name_plural = 'Зображення продукту'


class Reviews(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    review = models.TextField(max_length=1024, blank=True, null=True, default=None)
    user_name = models.CharField(max_length=68, blank=True, null=True, default=None)
    id_of_product = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'

    def __str__(self):
        return f'{self.review}'

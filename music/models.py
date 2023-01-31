from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title

class Music(models.Model):
    COUNTRY = (
        ('KG', 'Кыргызстан'),
        ('RU', 'Россия'),
        ('EN', 'Америка'),
    )

    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country = models.CharField(max_length=50, choices=COUNTRY)
    diration = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title} --- {self.category}'

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
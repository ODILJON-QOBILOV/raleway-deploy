from django.db import models

# Create your models here.


class BaseSlug(models.Model):
    slug = models.SlugField(unique=True)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        count = 0

        super().save(*args, force_insert=force_insert, force_update=force_update, using=using,update_fields=update_fields)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=555)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='books/', null=True, blank=True)
    amount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    author = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    book_is_atp = models.BooleanField(default=True)
    book_category = models.CharField(max_length=50)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'


#class Categories(models.Model):

#class E_Books(models.Model):

class Bindings(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    bind_size = models.CharField(max_length=200, null=True, blank=True)
    book_is_hardcover = models.BooleanField(default=True)
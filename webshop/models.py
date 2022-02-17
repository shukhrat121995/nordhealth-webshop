from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, MinValueValidator
from taggit.managers import TaggableManager


class Department(models.Model):
    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class Country(models.Model):
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(
        upload_to='images/products/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg']),
        ],
        blank=True
    )
    code = models.CharField(max_length=50, blank=False, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=False)
    origin = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField(blank=False, validators=[MinValueValidator(0.1)])
    weight = models.FloatField(blank=False, validators=[MinValueValidator(0.1)])
    quantity = models.IntegerField(blank=False, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name


class Blog(models.Model):
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    title = models.CharField(max_length=100, blank=False)
    image = models.ImageField(
        upload_to='images/blogs/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg']),
        ],
        blank=False
    )
    description = models.TextField(blank=False)
    date = models.DateField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class Contact(models.Model):
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=25, blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name

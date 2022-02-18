from django.test import TestCase
from django.contrib.auth.models import User
from webshop.models import Department, Country, Product, Blog, Contact
from datetime import date


class TestModels(TestCase):
    def setUp(self) -> None:
        user = User.objects.create(
            username='admin',
            first_name='Shukhrat',
            is_staff=True,
            is_active=True,
            is_superuser=True,
            password='HelloWord',
        )
        department = Department.objects.create(
            name='Fruits',
        )
        country = Country.objects.create(
            name='Brazil'
        )
        Product.objects.create(
            name='Banana',
            description='Bananas from Brazil',
            image='https://www.collinsdictionary.com/images/full/banana_64728013.jpg',
            code='baba-123',
            department=department,
            origin=country,
            price=2.5,
            weight=1.2,
            quantity=100,
        )
        Blog.objects.create(
            title='Can you eat a banana in cough and cold?',
            description='Banana is a fruit for all. It’s available throughout the year, affordable, nutritious, and '
                        'tasty and of course easy to eat – what else you need?',
            date=date.today(),
            author=user,
            tags=['banana', 'healthy-life']
        )

    def test_user_object(self):
        user = User.objects.get(username='admin')
        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, True)

    def test_department_object(self):
        department = Department.objects.get(name='Fruits')
        self.assertEqual(department.name, 'Fruits')

    def test_country_object(self):
        country = Country.objects.get(name='Brazil')
        self.assertEqual(country.name, 'Brazil')

    def test_product_object(self):
        product = Product.objects.get(code='baba-123')
        self.assertEqual(product.name, 'Banana')
        self.assertEqual(product.description, 'Bananas from Brazil')
        self.assertEqual(product.image, 'https://www.collinsdictionary.com/images/full/banana_64728013.jpg')
        self.assertEqual(product.code, 'baba-123')
        self.assertEqual(product.department.name, 'Fruits')
        self.assertEqual(product.origin.name, 'Brazil')
        self.assertEqual(product.price, 2.5)
        self.assertEqual(product.weight, 1.2)
        self.assertEqual(product.quantity, 100)

    def test_blog_object(self):
        blog = Blog.objects.get(id=1)
        self.assertEqual(blog.title, 'Can you eat a banana in cough and cold?')
        self.assertEqual(blog.description, 'Banana is a fruit for all. It’s available throughout the year, '
                                           'affordable, nutritious, and '
                                           'tasty and of course easy to eat – what else you need?')
        self.assertEqual(blog.date, date.today())
        self.assertEqual(blog.author.first_name, 'Shukhrat')

from django.test import TestCase, Client
from django.urls import reverse
from webshop.models import Department, Country, Product


class TestViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.shop_url = reverse('shop')
        self.product_details_url = reverse('product-details', args=['baba-123'])
        self.about_url = reverse('about')
        self.blog_url = reverse('blog')
        self.blog_details_url = reverse('blog-details', args=[1])
        department = Department.objects.create(
            name='Fruits'
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

    def test_shop_index_GET(self):
        response = self.client.get(self.shop_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'webshop/shop.html')

    def test_product_details_GET(self):
        response = self.client.get(self.product_details_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'webshop/product-details.html')

    def test_about_GET(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'webshop/about.html')

    def test_blog_GET(self):
        response = self.client.get(self.blog_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'webshop/blog.html')

    def test_blog_details_GET(self):
        response = self.client.get(self.blog_details_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'webshop/blog-details.html')

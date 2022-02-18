from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import shop, about, contact, blog, blog_details, product_details


class TestUrls(SimpleTestCase):
    def test_shop_url_is_resolved(self):
        url = reverse('shop')
        self.assertEqual(resolve(url).func, shop)

    def test_product_details_url_is_resolved(self):
        url = reverse('product-details', args=['abc-123'])
        self.assertEqual(resolve(url).func, product_details)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_blog_url_is_resolved(self):
        url = reverse('blog')
        self.assertEqual(resolve(url).func, blog)

    def test_blog_details_url_is_resolved(self):
        url = reverse('blog-details', args=[1])
        self.assertEqual(resolve(url).func, blog_details)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)

from django.test import SimpleTestCase
from webshop.forms import ContactForm


class TestForms(SimpleTestCase):
    def test_contact_form_valid_data(self):
        form = ContactForm(data={
            'name': 'Shukhrat',
            'email': 'test@gmail.com',
            'message': 'Simple test message'
        })
        self.assertTrue(form.is_valid())

    def test_contact_form_not_valid_email(self):
        form = ContactForm(data={
            'name': 'Shukhrat',
            'email': 'testgmail.com',
            'message': 'Simple test message'
        })
        self.assertFalse(form.is_valid())

    def test_contact_form_not_valid_name(self):
        form = ContactForm(data={
            'name': '',
            'email': 'testgmail.com',
            'message': 'Simple test message'
        })
        self.assertFalse(form.is_valid())

    def test_contact_form_not_valid_message(self):
        form = ContactForm(data={
            'name': 'Shukhrat',
            'email': 'testgmail.com',
            'message': ''
        })
        self.assertFalse(form.is_valid())




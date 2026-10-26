from django.test import TestCase
from django.urls import reverse


class PageViewTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Welcome to the Home Page!</h1>", html=True)

    def test_about_page(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "<h1>About Us</h1><p>This is the about page.</p>",
            html=True,
        )

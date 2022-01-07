from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="MADAO",
            subtitle="The Road of Gintama",
            author="Hasegawa Taizo",
            isbn="1234567890123",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "MADAO")
        self.assertEqual(self.book.subtitle, "The Road of Gintama")
        self.assertEqual(self.book.author, "Hasegawa Taizo")
        self.assertEqual(self.book.isbn, "1234567890123")
    
    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Road of Gintama")
        self.assertTemplateUsed(response, "books/book_list.html")
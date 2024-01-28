from django.views.generic import ListView
from books.models.books import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

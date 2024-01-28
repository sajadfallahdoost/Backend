from django.urls import path
from books.api.views import BookListView


urlpatterns = [
    path("books/", BookListView.as_view())
]

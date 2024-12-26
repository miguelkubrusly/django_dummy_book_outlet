from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from .models import Book


# Create your views here.


def index(req):
    books = Book.objects.all()
    return render(
        req,
        "book_outlet/index.html",
        {
            "books": books.order_by("title"),
            "total_book_num": books.count(),
            "average_rating": books.aggregate(Avg("rating")),
        },
    )


def details(req, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(
        req,
        "book_outlet/book-details.html",
        {
            "book": book,
        },
    )

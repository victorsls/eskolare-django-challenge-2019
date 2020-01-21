from rest_framework.serializers import ModelSerializer

from challenge.book.models import Book, Category, Author, Review


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'category', 'author')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ('evaluation', 'book', 'user')

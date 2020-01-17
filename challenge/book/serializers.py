from rest_framework.serializers import ModelSerializer

from challenge.book.models import Book, Category, Author, Review


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

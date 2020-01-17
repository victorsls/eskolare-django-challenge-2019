from rest_framework import routers

from challenge.book.views import BookViewSet, CategoryViewSet, AuthorViewSet, ReviewViewSet

app_name = 'book'

router = routers.SimpleRouter()
router.register('book', BookViewSet, basename='book')
router.register('category', CategoryViewSet, basename='category')
router.register('author', AuthorViewSet, basename='author')
router.register('review', ReviewViewSet, basename='review')
urlpatterns = router.urls

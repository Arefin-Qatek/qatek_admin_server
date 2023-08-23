from django.urls import path
from .views import ImageView,ImageListView

urlpatterns = [
    path('api/images/', ImageView.as_view()),
    path('api/images/<int:id>/', ImageView.as_view()),

    # Public URL pattern
    path('api/image-list/', ImageListView.as_view(), name='image-list-public'),
]

from django.urls import path
from .views import HomePageContentListView,HomePageContentPublicView

urlpatterns = [
    path('api/homepage/', HomePageContentListView.as_view(), name='homepage-content-list'),
    path('api/homepage/<int:id>/', HomePageContentListView.as_view(), name='homepage-content-detail'),

    # Public URL pattern
    path('api/homepage-list/', HomePageContentPublicView.as_view(), name='homepage-list-public'),
]

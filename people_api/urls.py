from django.urls import path
from .views import PeopleAPIView, PeopleDetail

urlpatterns = [
    path('', PeopleAPIView.as_view(), name='people'),
    path('people/', PeopleAPIView.as_view(), name='people'),
    path('people/<int:pk>/', PeopleDetail.as_view(), name='person_detail'),
]

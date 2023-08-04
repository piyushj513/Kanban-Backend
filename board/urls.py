from django.urls import path
from .views import UserListAPIView,CardListAPIView,UserLoginAPIView,UserRegistration,CommentsListAPIView

urlpatterns = [

        path('users/', UserListAPIView.as_view(), name='user-list'),
        path('login/', UserLoginAPIView.as_view(), name='user-login'),
        path('register/', UserRegistration.as_view(), name='user-register'),
        path('users/<str:pk>', UserListAPIView.as_view(), name='user-list2'),
        path('cards/', CardListAPIView.as_view(), name='card-list'),
        path('cards/<str:pk>', CardListAPIView.as_view(), name='card-list2'),
        # path('boards/', BoardListAPIView.as_view(), name='board-list'),
        # path('boards/<str:pk>', BoardListAPIView2.as_view(), name='board-list2'),
        # path('cols/', ColListAPIView.as_view(), name='col-list'),
        # path('cols/<str:pk>', ColListAPIView2.as_view(), name='col-list2'),
        path('comments/', CommentsListAPIView.as_view(), name='comment-list'),
        path('comments/<str:pk>', CommentsListAPIView.as_view(), name='comment-list2'),
]
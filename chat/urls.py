from django.urls import path

from .api import MessageList, MessageSingle, MessagePost


urlpatterns = [
    path('api/messages/list/<int:page_number>/', MessageList.as_view()),
    path('api/messages/single/<int:pk>/', MessageSingle.as_view()),
    path('api/messages/', MessagePost.as_view()),
]

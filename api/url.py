from django.urls import path
from .views import ChatView

urlpatterns = [
    path('chat/', ChatView.as_view(), name='chat'),
    # path('translate/', TranslateView.as_view(), name='translate'),
]
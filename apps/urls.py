from django.urls import path
from .views import English, Ielts

urlpatterns = [
    path('', English.as_view()),
    # path('', Ielts.as_view()),
]

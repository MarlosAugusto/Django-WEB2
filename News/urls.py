from django.urls import path, include
from .views import home, new

urlpatterns = [
  path('', home, name='home'),
  path('new/<int:codigo>', new, name='new'),
]
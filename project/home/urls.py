from django.urls import path
from home.views import MainView

urlpatterns = [
    path('home/', MainView.as_view(), name="home")
]
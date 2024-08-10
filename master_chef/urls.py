from django.urls import path

from master_chef.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]

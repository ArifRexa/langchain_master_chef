from django.urls import path

from master_cheif.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]

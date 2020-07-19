from django.urls import path,include
from order import views

urlpatterns = [
    path('option/',views.OrderAPIView.as_view())
]
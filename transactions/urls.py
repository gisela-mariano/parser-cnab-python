from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'transactions', views.TransactionCreateListView, basename='upload')

urlpatterns = [
    path("", include(router.urls)),
    path("transactions/<str:id_transaction>/", views.TransactionDetailView.as_view()),
]

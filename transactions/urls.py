from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("transactions/<filename>/", views.TransactionCreateView.as_view()),
    path("transactions/", views.TransactionListView.as_view()),
    path("transactions/<str:id_transaction>/", views.TransactionDetailView.as_view()),
]

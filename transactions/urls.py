from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# router.register(r"transactions", views.TransactionCreateListView, basename="upload")

urlpatterns = [
    path("form/", views.Teste, name="form"),
    # path("", include(router.urls), name="upload"),
    # path(r"transactions", views.TransactionCreateListView.as_view({'get': 'list', 'post': 'create'}), name="upload"),
    path("transactions/<str:id_transaction>/", views.TransactionDetailView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
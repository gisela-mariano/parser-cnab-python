from base64 import encode
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.parsers import FileUploadParser

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from .models import Transaction
from .serializers import TransactionSerializer

from django.conf import settings
import os


class TransactionCreateView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, filename):
        file = request.FILES["file"]

        path = default_storage.save(f"tmp/{filename}", ContentFile(file.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

        with open(tmp_file, "r", encoding="utf-8") as f:

            data_file = f.read().splitlines()

            for row in data_file:
                trated_row = row.rstrip()

                trated_value = int(row[9:19]) / 100

                Transaction.objects.create(
                    type=int(trated_row[0:1]),
                    date=trated_row[1:9],
                    value=trated_value,
                    cpf=trated_row[19:30],
                    card=trated_row[30:42],
                    hour=trated_row[42:48],
                    store_owner=trated_row[48:62],
                    store_name=trated_row[62:-1],
                )

        os.remove(tmp_file)

        return Response(status=status.HTTP_201_CREATED)


class TransactionListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetailView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_url_kwarg = "id_transaction"

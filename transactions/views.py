from django.shortcuts import render
from rest_framework import generics, status

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import Transaction
from .serializers import TransactionSerializer, FileSerializer

from django.conf import settings
import os


class TransactionCreateListView(ViewSet):
    serializer_class = FileSerializer

    def list(self, request):
        transactions = Transaction.objects.all()

        json_file = TransactionSerializer(transactions, many=True)

        return Response(json_file.data, status.HTTP_200_OK)

    def create(self, request):
        file_uploaded = request.FILES.get("file_uploaded")
        filename = file_uploaded.name
        content_type = file_uploaded.content_type

        path = default_storage.save(
            f"tmp/{filename}", ContentFile(file_uploaded.read())
        )
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
                    store_name=trated_row[62:],
                )

        os.remove(tmp_file)

        transactions = Transaction.objects.all()

        json_file = TransactionSerializer(transactions, many=True)

        return Response(json_file.data, status.HTTP_200_OK)


class TransactionDetailView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_url_kwarg = "id_transaction"

from multiprocessing import context
from django.shortcuts import render
from rest_framework import generics, status

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import UnsupportedMediaType, NotFound

from .models import Transaction
from .serializers import TransactionSerializer #, FileSerializer

from django.conf import settings
import os
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.forms.models import model_to_dict

import ipdb
import ast


@csrf_exempt
def Teste(request):

    file_system = FileSystemStorage()

    context = {}

    if request.method == "POST":
        Transaction.objects.all().delete()

        file = request.FILES["doc"]
        filename = file.name
        file_system.save(file.name, file)

        payments = [2, 3, 9]

        path = f"media/{filename}"

        with open(path, "r", encoding="utf-8") as f:

            data_file = f.read().splitlines()

            for row in data_file:
                trated_row = row.rstrip()
                trated_type = int(trated_row[0:1])
                trated_value = int(row[9:19]) / 100

                if trated_type in payments:
                    trated_value *= -1

                Transaction.objects.create(
                    type=trated_type,
                    date=trated_row[1:9],
                    value="%.2f" % trated_value,
                    cpf=trated_row[19:30],
                    card=trated_row[30:42],
                    hour=trated_row[42:48],
                    store_owner=trated_row[48:62].rstrip(),
                    store_name=trated_row[62:],
                )

        file_system.delete(filename)

    transactions = Transaction.objects.all()

    # json_file = TransactionSerializer(transactions, many=True)
    json_file = [model_to_dict(transaction) for transaction in transactions]

    total_value = 0

    for item in json_file:
        # ipdb.set_trace()
        total_value += float(item["value"])

    context["transactions"] = json_file
    context["total_value"] = total_value

    return render(request, "form.html", context=context)


# class TransactionCreateListView(ViewSet):
#     serializer_class = FileSerializer

#     def list(self, request):
#         transactions = Transaction.objects.all()

#         json_file = TransactionSerializer(transactions, many=True)

#         return Response(json_file.data, status.HTTP_200_OK)

#     def create(self, request):
#         # file_uploaded = request.FILES.get("file_uploaded")
#         file_uploaded = request.FILES.get("uploaded_file")

#         import ipdb

#         ipdb.set_trace()

#         if file_uploaded == None:
#             raise NotFound(detail="You need to send a file.")

#         content_type = file_uploaded.content_type

#         if content_type != "text/plain":
#             raise UnsupportedMediaType(
#                 media_type=content_type, detail="Supported only text file."
#             )

#         filename = file_uploaded.name

#         path = default_storage.save(
#             f"tmp/{filename}", ContentFile(file_uploaded.read())
#         )
#         tmp_file = os.path.join(settings.MEDIA_ROOT, path)

#         payments = [2, 3, 9]

#         with open(tmp_file, "r", encoding="utf-8") as f:

#             data_file = f.read().splitlines()

#             for row in data_file:
#                 trated_row = row.rstrip()
#                 trated_type = int(trated_row[0:1])
#                 trated_value = int(row[9:19]) / 100

#                 if trated_type in payments:
#                     trated_value *= -1

#                 Transaction.objects.create(
#                     type=trated_type,
#                     date=trated_row[1:9],
#                     value="%.2f" % trated_value,
#                     cpf=trated_row[19:30],
#                     card=trated_row[30:42],
#                     hour=trated_row[42:48],
#                     store_owner=trated_row[48:62].rstrip(),
#                     store_name=trated_row[62:],
#                 )

#         os.remove(tmp_file)

#         transactions = Transaction.objects.all()

#         json_file = TransactionSerializer(transactions, many=True)

#         return Response(json_file.data, status.HTTP_200_OK)


class TransactionDetailView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_url_kwarg = "id_transaction"

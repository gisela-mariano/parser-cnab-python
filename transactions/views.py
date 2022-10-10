from django.shortcuts import render

from rest_framework.exceptions import UnsupportedMediaType, NotFound, NotAcceptable

from .models import Transaction

from django.conf import settings
import os
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.forms.models import model_to_dict


@csrf_exempt
def CreateListTransactions(request):

    file_system = FileSystemStorage()

    context = {}
    errors = {}

    context["errors"] = errors
    file_errored = False

    Transaction.objects.all().delete()

    if request.method == "POST":

        if request.POST.get("doc") == "":
            errors["not_found"] = "Você deve enviar um arquivo."
            # raise NotFound(detail="You must send a file.")
            return render(request, "form.html", context=context)

        file = request.FILES["doc"]
        filename = file.name
        file_system.save(file.name, file)

        payments = [2, 3, 9]

        path = f"media/{filename}"

        with open(path, "r", encoding="utf-8") as f:

            data_file = f.read().splitlines()

            for row in data_file:
                if len(row) != 80:
                    file_errored = True

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

    if file_errored:
        errors[
            "invalid_format"
        ] = "Formato de CNAB inválido. Cada código CNAB deve conter 80 caracteres."
        return render(request, "form.html", context=context)

    transactions = Transaction.objects.all()
    json_file = [model_to_dict(transaction) for transaction in transactions]

    total_value = 0

    for item in json_file:
        total_value += float(item["value"])

    context["transactions"] = json_file
    context["total_value"] = "%.2f" % total_value

    return render(request, "form.html", context=context)

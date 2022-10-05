from rest_framework import serializers

from .models import Transaction, File


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class FileSerializer(serializers.Serializer):
    file_uploaded = serializers.FileField()
    class Meta:
        # model = File
        # fields = "__all__"
        fields = ['file_uploaded']

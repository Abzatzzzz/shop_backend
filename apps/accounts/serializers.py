from rest_framework import serializers

from apps.accounts.models import Account


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("user_id", "status", "created_at", "updated_at")
        read_only_fields = fields

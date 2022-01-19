import factory
from django.contrib.auth.models import User

from apps.accounts.models import Account


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:

        model = User

    username = "Test_user"


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    user = factory.SubFactory(UserFactory)

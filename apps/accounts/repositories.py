from apps.accounts.models import Account


class AccountModelRepository:
    @staticmethod
    def get_all():
        return Account.objects.all()

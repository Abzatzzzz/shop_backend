from rest_framework.generics import ListAPIView

from .repositories import AccountModelRepository
from .serializers import AccountListSerializer


class AccountListView(ListAPIView):
    serializer_class = AccountListSerializer
    queryset = AccountModelRepository.get_all()

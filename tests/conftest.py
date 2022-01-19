import pytest
from pytest_factoryboy import register

from tests import factories

register(factories.AccountFactory)


@pytest.fixture
def account(db, account_factory):

    return account_factory()

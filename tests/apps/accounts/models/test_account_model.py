class TestAccountModel:
    def test_str_method(self, account):
        username = account.user.username
        status = account.status
        assert str(account) == f"{username}-{status}"

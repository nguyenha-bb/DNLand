from django.db import models
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.hashers import check_password

class AccountBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            account = Account.objects.get(username=username)
            if account.password == password:  # Đảm bảo mã hóa mật khẩu trong ứng dụng thực tế
                return account
        except Account.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return None

class Role(models.Model):
    roleName = models.CharField(max_length=20)
    class Meta:
        db_table = 'Roles'

# class Account(models.Model):
#     fullname = models.CharField(max_length=100)
#     username = models.CharField(max_length=100, unique=True)
#     password = models.CharField(max_length=100)
#     phoneNumber = models.CharField(max_length=10)
#     role = models.ForeignKey(Role, on_delete=models.CASCADE)
#     class Meta:
#         db_table = 'Accounts'

class Account(AbstractBaseUser):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=10)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'Accounts'

    def __str__(self):
        return self.username

    @property
    def is_authenticated(self):
        return True





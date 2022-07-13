from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=155)
    number = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=80)
    city = models.CharField(max_length=100)

    user = models.OneToOneField(
        "accounts.Account", on_delete=models.CASCADE, related_name="address"
    )

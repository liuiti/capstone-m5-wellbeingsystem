from django.db import models

# Create your models here.


class Receipt(models.Model):
    price = models.FloatField()
    payed = models.BooleanField(default=False)
    input_date = models.DateField(auto_now_add=True)
    output_date = models.DateField(auto_now=True)

    works = models.ForeignKey(
        "works.Work", on_delete=models.CASCADE, related_name="receipts"
    )

    contractor = models.OneToOneField(
        "accounts.Account", on_delete=models.CASCADE, related_name="receipts"
    )

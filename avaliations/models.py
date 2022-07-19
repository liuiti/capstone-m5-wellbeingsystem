from django.db import models


class Avaliation(models.Model):
    comment = models.CharField(max_length=200, null=True)
    stars = models.IntegerField()

    receipt = models.ForeignKey(
        "receipts.Receipt", on_delete=models.CASCADE, related_name="avaliations"
    )

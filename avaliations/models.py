from django.db import models

# Create your models here.


class Avaliation(models.Model):
    comment = models.CharField(max_length=200)
    stars = models.IntegerField()

    receipt = models.OneToOneField(
        "receipts.Receipt", on_delete=models.CASCADE, related_name="avaliations"
    )

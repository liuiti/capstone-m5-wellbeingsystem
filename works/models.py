from django.db import models

# Create your models here.


class Work(models.Model):
    name = models.CharField(max_length=100)

    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="works"
    )

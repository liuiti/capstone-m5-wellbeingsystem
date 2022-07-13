import uuid
from django.db import models

# Create your models here.


class Work(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="works"
    )

    user = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="works"
    )

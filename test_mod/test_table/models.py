from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Imginfo(models.Model):
    img_id = models.CharField(max_length=100)
    metadata = models.TextField()
    img_datetime = models.DateTimeField(default=timezone.now)
    current_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.img_id

    class Meta:
        managed = False


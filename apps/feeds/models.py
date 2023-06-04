from django.db import models
from sorl.thumbnail import ImageField


class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)
    image = ImageField(upload_to="images", default="default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.text}"

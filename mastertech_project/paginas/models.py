import uuid
from django.db import models
from django.urls import reverse
# Create your models here.

class Livros(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
    titulo = models.CharField(max_length=60)
    autor = models.CharField(max_length=60)
    dispon = models.CharField(max_length=5)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('book_details',args=[str(self.id)])




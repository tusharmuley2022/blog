from django.db import models
from account.models import CustomUser

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #created_by = models.IntegerField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}+' by '+{self.created_by}"
    
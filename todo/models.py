from django.db import models
# reference user model to todo model
from django.contrib.auth import get_user_model
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # many todo to one user relationship
    posted_by = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=models.CASCADE  # user/todo cascade delete
    )

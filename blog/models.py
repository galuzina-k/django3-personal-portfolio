from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=False)
    description = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

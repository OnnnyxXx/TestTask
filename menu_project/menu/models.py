from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=120)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=150, blank=True)
    name_url = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.title


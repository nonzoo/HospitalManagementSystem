from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    capacity = models.PositiveIntegerField()


    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Hospital'

    def __str__(self):
        return self.name
from django.db import models


class View(models.Model):
    ip_address = models.GenericIPAddressField(default="10.0.0.0")
    count = models.IntegerField(default=0)

    def __str__(self):
        return 'IP: {0}, Count:{1}'.format(self.ip_address, self.count)

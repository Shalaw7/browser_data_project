from django.db import models

from django.db import models

class BrowserData(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    screen_resolution = models.CharField(max_length=50)
    device_type = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.user_agent[:30]}"

from django.db import models

# Create your models here.

class LottoDraw(models.Model):
    numbers = models.JSONField()  # 6 sayı listesi (örn: [4, 12, 23, 35, 41, 48])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.numbers} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

from django.db import models

class Application(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('OA', 'Online Assessment'),
        ('Interview', 'Interview'),
        ('Offer', 'Offer'),
        ('Rejected', 'Rejected'),
    ]

    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')
    applied_date = models.DateField(null=True, blank=True)
    next_step_due = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company} — {self.role}"
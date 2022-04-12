from django.db import models




# Create your models here.
class Todo (models.Model) : 
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )

    title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='pending')

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title
from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Car(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="cars")
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    vin = models.CharField(max_length=17, unique=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class RepairOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('in_progress', 'В работе'),
        ('completed', 'Завершен'),
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="repairs")
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ремонт {self.car} - {self.get_status_display()}"

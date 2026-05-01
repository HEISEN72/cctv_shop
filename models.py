from django.db import models

class Buyer(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Camera(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cameras/', blank=True, null=True)

    def __str__(self):
        return self.title

class CartItem(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.buyer.username} - {self.camera.title}"
from django.db import models

# Create your models here.
class core(models.Model):
    hey=models.CharField(max_length=50)

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    testimonial_text = models.TextField()

    def __str__(self):
        return self.client_name
    



class Contact(models.Model):  # Use PascalCase for the class name
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
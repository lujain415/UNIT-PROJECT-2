from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=[
            ('dog', 'Dog'),
            ('cat', 'Cat'),
            ('bird', 'Bird'),
            ('other', 'Other'),
        ]
    )
    description = models.TextField()
    image = models.ImageField(upload_to='pet_images/', null=True, blank=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.pet.name}"

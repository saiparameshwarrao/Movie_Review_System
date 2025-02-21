from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='movies/', null=True, blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews", null=True, blank=True)
    director = models.CharField(max_length=200, blank=True, null=True)  
    genre = models.CharField(max_length=100, blank=True, null=True) 
    release_date = models.DateField(blank=True, null=True) 
    synopsis = models.TextField(blank=True, null=True)  
    spoiler = models.TextField(blank=True, null=True) 
    image = models.ImageField(upload_to='movies/', blank=True, null=True)



class UserReview(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="user_reviews")
    username = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.movie.name} ({self.rating}/5)"

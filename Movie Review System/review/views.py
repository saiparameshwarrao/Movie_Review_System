from django.shortcuts import render, get_object_or_404
from .models import Movie

def index(request):
    movies = Movie.objects.all()  
    return render(request, 'index.html', {'movies': movies})

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Review, UserReview

def movie_detail(request, movie_name):
    movie = get_object_or_404(Movie, name=movie_name)
    user_reviews = UserReview.objects.filter(movie=movie)  # Fetch user reviews
    movie_review = Review.objects.filter(movie=movie).first()  # Fetch detailed review info

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to submit a review.")
            return redirect('login')  # Redirect to login page

        username = request.user.username  # Use logged-in user's name
        review_text = request.POST.get("review_text")
        rating = request.POST.get("rating")

        if review_text and rating:
            UserReview.objects.create(
                movie=movie,
                username=username,
                review_text=review_text,
                rating=int(rating)
            )
            messages.success(request, "Your review has been submitted successfully!")
            return redirect('movie_detail', movie_name=movie_name)  
        
    return render(request, 'movie_detail.html', {
        'movie': movie,
        'user_reviews': user_reviews,
        'movie_review': movie_review
    })


def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

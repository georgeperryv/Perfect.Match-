from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000
    path('', views.home, name='home'),
    path('log-in/', views.log_in, name='log_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('job-listings/', views.job_listings, name = 'job_listings'),
    path('job-matches/', views.job_matches, name='job_matches'),
    path('saved-jobs/', views.saved_jobs, name='saved_jobs'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name = 'about'),
]

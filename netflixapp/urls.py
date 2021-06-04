from django.urls import path, include
from . import views

urlpatterns = [
    path('in/', views.home, name='in'),
    path('in/login/', views.LoginPage, name='login'),
    path('in/signup/', views.SignUpFirst, name='signupfirst'),
    path('in/signup/RegForm', views.SignUpSecond, name='signupsecond'),
    path('in/signup/plan', views.SignUpThird, name='signupthird'),
    path('in/signup/planform', views.SignUpFourth, name='signupfourth'),
    path('in/signup/payment', views.SignUpFifth, name='signupfifth'),
    path('in/signup/creditoption', views.SignUpSixth, name='signupsixth'),
    path('in/dashboard/', views.Dashboard, name='dashboard'),
    path('in/dashboard/movie/<int:id>/', views.Movie, name='movie'),
    path('in/dashboard/tvseries', views.TVSeries, name='tvseries'),
    path('in/dashboard/movies', views.Movies, name='movies'),
    path('in/logout/', views.LogoutPage, name='logout'),

    path('', include('netflixapp.API.urls'))
]
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile/', views.userProfile, name = "user-profile"),

    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutuser, name='logout'),
    path('register/',views.registerUser, name='register'),

    path('video/', views.videoList, name="video-list"),
    path('watch/<str:pk>', views.watchVideo, name="watch-video"),

    path('delete/<str:pk>', views.deleteComment, name = "delete-comment"),

    path('update_user/', views.update_user, name="update-user"),

    path('live/', views.live, name="live"),
    path('schedule/', views.schedule, name="schedule"),
    path('medal/', views.medal, name="medal"),
    path('about/', views.about, name="about"),

        
    # reset password urls############
    path('password_reset/',auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    ############


]






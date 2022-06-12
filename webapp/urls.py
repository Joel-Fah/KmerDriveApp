from django.urls import path
from .views import HomeView, ContactView, SignUpView, LoginView, LogoutView, ActionsView, AccountView, UpdateProfileView, UpdateUserView, NavigationView

# Create your urls here

app_name = 'webapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('app/<str:pk>/<str:user>/', ActionsView.as_view(), name='app'),
    path('app/<str:pk>/<str:user>/account/', AccountView.as_view(), name='account'),
    path('app/<str:pk>/<str:user>/account/update-profile-info', UpdateProfileView.as_view(), name='update_user'),
    path('app/<str:pk>/<str:user>/account/update-user-info', UpdateUserView.as_view(), name='update_profile'),
    path('app/<str:pk>/<str:user>/navigation/', NavigationView.as_view(), name='navigation'),
]

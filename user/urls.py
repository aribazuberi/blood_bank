from django.urls import path
from . import views

from user.views import(
	registration_view,
	logout_view,
	login_view,
	update_view,
)


urlpatterns = [
    path('', views.home, name='user-home'),
    path('profile/', views.profile, name='user-profile'),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('update/', update_view, name="update"),
]
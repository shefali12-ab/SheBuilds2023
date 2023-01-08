from django.urls import path
from .views import *

urlpatterns = [
    path('login', login_page, name="login"),
    path('register', register, name="register"),
    path('', homepage, name="homepage"),
    path('logout', logout_page, name="logout"),
    path('diagnosis', quiz, name="quiz"),
    path('discussion', discussion, name="discussion"),
    path('discussion/add', add_discussion, name="add_discussion"),
    path('discussion/view/<int:pk>', view_discussion, name="view_discussion")
]
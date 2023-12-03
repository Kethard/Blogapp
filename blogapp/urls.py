
from django.urls import path
from blogapp import views

urlpatterns = [
    path('post/<slug:slug>',views.post_page, name = 'post_page'),
]

from django.urls import path
from . import views

urlpatterns =[
    path("", views.ArticleView.as_view(), name="article_view"),
    path("<int:article_id>/", views.ArticleDetailView.as_view(), name="article_detial_view"),
]
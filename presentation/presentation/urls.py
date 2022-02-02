"""presentation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from topic_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TopicListListView.as_view(), name='topic-list'),
    path('topic/<int:pk>/', views.TopicListDetailView.as_view(), name='topic-detail'),
    path('topic/create/', views.TopicListCreateView.as_view(), name='topic-create'),
    path('topic/update/<int:pk>/', views.TopicListUpdateView.as_view(), name='topic-update'),
    path('topic/delete/<int:pk>/', views.TopicListDeleteView.as_view(), name='topic-delete'),
]

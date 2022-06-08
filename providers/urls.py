from django.urls import path

from . import views


urlpatterns = [
    path('', views.provider_list_create_view),
    path('<int:pk>/update/', views.provider_update_view),
    path('<int:pk>/delete/', views.provider_destroy_view),
    path('<int:pk>/', views.provider_detail_view),
]

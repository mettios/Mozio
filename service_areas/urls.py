from django.urls import path

from . import views


urlpatterns = [
    # path('', views.service_area_list_create_view),
    # path('<int:pk>/update/', views.service_area_update_view),
    # path('<int:pk>/delete/', views.service_area_destroy_view),
    # path('<int:pk>/', views.service_area_detail_view)
    path('', views.service_area_list_create_view),
    path('<int:pk>/update/', views.service_area_update_view),
    path('<int:pk>/delete/', views.service_area_destroy_view),
    path('<int:pk>/', views.service_area_detail_view)
]



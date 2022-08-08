from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('fish/', views.fish_index, name='fish_index'),
  path('fish/<int:fish_id>/', views.fish_detail, name='fish_detail'),
  path('fish/create/', views.FishCreate.as_view(), name='fish_create'),
  path('fish/<int:pk>/update/', views.FishUpdate.as_view(), name='fish_update'),
  path('fish/<int:pk>/delete/', views.FishDelete.as_view(), name='fish_delete'),
  path('fish/<int:fish_id>/add_catch/', views.add_catch, name='add_catch'),
  path('fish/<int:fish_id>/assoc_lure/<int:lure_id>/', views.assoc_lure, name='assoc_lure'),
  path('lures/create/', views.LureCreate.as_view(), name='lure_create'),
  path('lures/<int:pk>/', views.LureDetail.as_view(), name='lure_detail'),
  path('lures/', views.LureList.as_view(), name='lures_index'),
  path('lures/<int:pk>/update/', views.LureUpdate.as_view(), name='lures_update'),
  path('lures/<int:pk>/delete/', views.LureDelete.as_view(), name='lures_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]
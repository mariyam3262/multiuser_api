from django.urls import path
from .views import *

app_name = 'product'
urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('list/', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/detail/', ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    #----------------------------------Collection-----------------------------------------

    path('collection-create/', CollectionCreateView.as_view(), name='collection-create'),
    path('collection-list/', CollectionListView.as_view(), name='collection-list'),
    path('collection/<int:pk>/detail/', CollectionDetailView.as_view(), name='collection-detail'),
    path('collection/<int:pk>/update/', CollectionUpdateView.as_view(), name='collection-update'),
    path('collection/<int:pk>/delete/', CollectionDeleteView.as_view(), name='collection-delete'),

    # ----------------------------------Size---------------------------------------------------


    path('size-create/', SizeCreateView.as_view(), name='size-create'),
    path('size-list/', SizeListView.as_view(), name='size-list'),
    path('size/<int:pk>/detail/', SizeDetailView.as_view(), name='size-detail'),
    path('size/<int:pk>/update/', SizeUpdateView.as_view(), name='size-update'),
    path('size/<int:pk>/delete/', SizeDeleteView.as_view(), name='size-delete'),

    # -----------------------------Thickness---------------------------------------------------


    path('thickness-create/', ThicknessCreateView.as_view(), name='thickness-create'),
    path('thickness-list/', ThicknessListView.as_view(), name='thickness-list'),
    path('thickness/<int:pk>/detail/', ThicknessDetailView.as_view(), name='thickness-detail'),
    path('thickness/<int:pk>/update/', ThicknessUpdateView.as_view(), name='thickness-update'),
    path('thickness/<int:pk>/delete/', ThicknessDeleteView.as_view(), name='thickness-delete'),

     # -----------------------------Thickness---------------------------------------------------


    path('surface-create/', SurfaceCreateView.as_view(), name='surface-create'),
    path('surface-list/', SurfaceListView.as_view(), name='surface-list'),
    path('surface/<int:pk>/detail/', SurfaceDetailView.as_view(), name='surface-detail'),
    path('surface/<int:pk>/update/', SurfaceUpdateView.as_view(), name='surface-update'),
    path('surface/<int:pk>/delete/', SurfaceDeleteView.as_view(), name='surface-delete'),
]
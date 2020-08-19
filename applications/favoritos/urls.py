from django.urls import path
from . import views

app_name = 'favoritos_app'

urlpatterns = [
    path('perfil/', views.UserPageView.as_view(), name='perfil'),
    path('add-entrada/<pk>', views.addFavoritesView.as_view(), name='add-favoritos'),
    path('delete-favorite/<pk>', views.FavoritesDeleteView.as_view(), name='delete-favoritos')
]

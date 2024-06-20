from django.urls import path
from . import views


from django.views.generic import TemplateView

app_name = 'Liga'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('hrac/', views.HracListView.as_view(), name='hrac_list'),
    path('hrac/<int:pk>/', views.HracDetailView.as_view(), name='hrac_detail'),
    path('tym/', views.TymListView.as_view(), name='tym_list'),
    path('tym/<int:pk>/', views.TymDetailView.as_view(), name='tym_detail'),
    path('liga/', views.LigaListView.as_view(), name='liga_list'),
    path('liga/<int:pk>/', views.LigaDetailView.as_view(), name='liga_detail'),
    path('zapas', views.ZapasListView.as_view(), name='zapas_list'),
    path('zapas/<int:pk>/', views.ZapasDetailView.as_view(), name='zapas_detail'),
]

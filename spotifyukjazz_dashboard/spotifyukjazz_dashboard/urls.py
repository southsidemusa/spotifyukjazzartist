
# urls.py
from django.urls import path
from .views import table, chart


urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('all_repos/', views.all_repos),
    path('table/', views.table_view),    
    path('chart/', views.chart_view),
    path('homepage/', views.homepage_view),
]
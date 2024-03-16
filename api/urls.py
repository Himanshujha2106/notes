from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.getRoutes,name="routes"),
    path('notes/',views.getnotes,name="notes"),
    path('notes/<str:pk>/',views.getnote,name="note"),

]

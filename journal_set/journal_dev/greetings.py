from . import views
from django.urls import path

urlpatterns = [
    path('', views.greetings, name ='greetings'),
    path('filter/', views.FilterList, name='filter'),
    path('create/', views.Create, name ='create'),
    path('detail/<int:id>', views.Detail, name ='detail'),
    path('update/<int:id>', views.Update, name ='update'),
    path('delete/<int:id>', views.Delete, name ='delete'),
    #path('mark/<int:id>', views.Mark, name ='marks'),
    path('exportcsv/', views.exportcsv, name ='exportcsv'),

]
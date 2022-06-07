from django.urls import path
from . import views

app_name = 'helpdeskapp'

urlpatterns = [
    path('adds/', views.adds, name='adds'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('mylist/', views.mylist, name='mylist'),
    path('query_data/', views.query_data, name='query_data'),
    path('doaction/<action>', views.DoAction, name='DoAction'),
    path('export_pdf/', views.export_pdf, name='export-pdf'),
    path('export_excel/', views.export_excel, name='export-excel'),
    path('export_blank_pdf/', views.export_blank_pdf, name='export-blank-pdf'),
]
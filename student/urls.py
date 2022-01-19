
from django.urls import path, include
from . import views

app_name = 'student'

urlpatterns = [
   path('add/',views.add_page,name='add'),
   path('add_save/',views.add_save,name='add_save'),
   path('index/',views.index,name='index'),
   path('<int:students_id>/edit/',views.edit,name='edit'),
   path('edit_save/',views.edit_save,name='edit_save'),
   path('<int:students_id>/delet_students/',views.delet_students,name='delet_students'),
]
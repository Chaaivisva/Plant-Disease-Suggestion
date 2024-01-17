from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.index, name="index"),

  #Credential
  path('login/', views.login, name='login'),
  path('signup/', views.register, name='register'),
  path('logout/', views.logout_view, name='logout'),

  #User_page
  path('plant_library/', views.user_page1, name="user_page1"),
  path('plant_description/<int:plant_id>/', views.plant_description, name="plant_description"),
  path('userProblem/', views.user_problem, name="user_problem"),
  path('add_problem/', views.add_problem, name="add_problem"),
  path('delete_problem/<int:comment_id>/', views.delete_comment, name="delete_comment"),
  path('comment/<int:plant_id>/', views.add_comment, name='add_comment'), 
  path('read_comment/<int:plant_id>/', views.read_comment, name="read_comment"),  
  path('daily_updates/', views.daily_updates, name="daily_updates"),


  #Manager
  path('manager/', views.manager, name="manager"),
  path('updates/', views.updates, name="updates"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
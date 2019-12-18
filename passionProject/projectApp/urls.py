from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   # path('all_user/', views.all_user, name='all_user'),
   # path('edit_deposit/', views.edit_deposit, name='edit_deposit'),
   # path('new_user/', views.new_user, name='new_user'),
   # path('accounts/login/', views.log_in, name='log_in'),
   # path('accounts/logout/', views.log_out, name='log_out'),
   path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
   path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('accounts/profile/', auth_views.LogoutView.as_view(), name='profile'),
   #TODO change views for profile to show profile of user.
   path('mine/', views.ManageCourseListView.as_view(), name='manage_course_list'),
   path('create/', views.CourseCreateView.as_view(), name='course_create'),
   path('<pk>/module/', views.CourseModuleUpdateView.as_view(), name='course_module_update'),
   path('<pk>/edit/', views.CourseUpdateView.as_view(), name='course_edit'),
   path('<pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
   path('module/<int:module_id>/content/<model_name>/create/', views.ContentCreateUpdateView.as_view(), name='module_content_create'),
   path('module/<int:module_id>/content/<model_name>/<id>/', views.ContentCreateUpdateView.as_view(), name='module_content_update'),
   path('module/<int:module_id>/', views.ModuleContentListView.as_view(), name='module_content_list'),
   path('content/<int:id>/delete/', views.ContentDeleteView.as_view(), name='module_content_delete'),
   path('module/order/', views.ModuleOrderView.as_view(), name='module_order'),
   path('content/order/', views.ContentOrderView.as_view(), name='content_order'),
   path('', views.index, name='index'),
]

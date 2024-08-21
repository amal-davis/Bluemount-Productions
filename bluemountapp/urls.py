from django.urls import path,re_path
from  bluemountapp import views
from  django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve



urlpatterns = [
    path('',views.index,name='index'),
    path('add_video',views.add_video,name='add_video'),
    path('delete_video/<int:video_id>',views.delete_video,name='delete_video'),
    path('edit_video/<int:video_id>/',views.edit_video,name='edit_video'),
    path('gallery_view',views.gallery_view,name='gallery_view'),
    path('delete_image/<int:image_id>/',views.delete_image,name='delete_image'),
    path('career_view',views.career_view,name='career_view'),
    path('delete_position/<int:position_id>/',views.delete_position,name='delete_position'),
    path('edit_position/<int:position_id>/',views.edit_position,name='edit_position'),
    path('contact_view',views.contact_view,name='contact_view'),
    path('contact_list_view',views.contact_list_view,name='contact_list_view'),
    path('delete_contact/<int:contact_id>/',views.delete_contact,name='delete_contact'),
    path('admin_page',views.admin_page,name='admin_page'),
    path('login_view',views.login_view,name='login_view')
]
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_home,name='getList'),
    path('load-districts', views.load_districts, name='loadDistricts'),
    path('load-wards', views.load_wards, name='loadWards'),
    # path('/home/<int:id>', views.view_home_page, name="homePage"),
    path('upload-post', views.view_upload_post, name='uploadPost'),
    path('detail-post/<int:id>', views.view_detail_post, name='detailPost'),
    path('detail-update-post/<int:id>', views.view_detail_update_post, name='detailUpdatePost'),
    path('update-post/<int:id>', views.view_update_post, name='updatePost'),
    path('delete-post/<int:id>', views.view_delete_post, name='deletePost'),
    path('manage-post', views.view_manage_post, name='managePost'),
    path('admin-action/censor-post', views.view_censor_post, name='censorPost'),
    path('admin-action/list-post', views.view_list_post_admin, name='listPostAdmin'),
]

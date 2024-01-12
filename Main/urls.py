
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.registration,name='home'),
    path('delete/<int:id>/',views.delete_stu,name='deletedata'),
    path('update/<int:id>/',views.update_stu,name='updatedata'),
]

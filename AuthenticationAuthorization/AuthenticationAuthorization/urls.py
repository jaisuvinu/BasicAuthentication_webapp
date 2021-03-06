
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from student import views

router =DefaultRouter()
router.register('studentapi',views.StudentModelViewSet,basename = 'student')
router.register('facultyapi',views.FacultyModelViewSet,basename = 'faculty')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]

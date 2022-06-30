from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, \
    DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

from student.models import Student, Faculty
from student.serializer import StudentSerializer, FacultySerializer


# Basic Authentication in local level(views)
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
   # permission_classes = [AllowAny]    #allow unrestricted access regardless of if the request is authnticated or unauthenticated
   # permission_classes = [IsAuthenticated] #this allow permissions to only authenticated persons to acces end points
   # permission_classes = [IsAdminUser] #only super user has permissions to access
   #permission_classes = [IsAuthenticatedOrReadOnly] #allow all permissions to authenticated users and only 'get' permissions to other users
    #permission_classes = [DjangoModelPermissions] # allows superuser for all end points but authorized permissions for authorized users
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]# allow authorised persons to access the permissions restricted to them and anonymous users can only read

#  authentication(settings.py)
class FacultyModelViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
from django.conf.urls import url, include
from rest_framework import routers
from .views import (UserListView, 
                    UserDetailView,
                    UserCreateAPIView,
                    UserLoginAPIView)


urlpatterns = [
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^(?P<pk>\d+)/$', UserDetailView.as_view(), name='detail'),
    url(r'^', UserListView.as_view(), name='list'), 

]















# from django.conf.urls import url, include
# from .views import (
#     SubjectListView,)
 


# urlpatterns = [
#     url(r'^list/', SubjectListView.as_view(), name='list'),
#     url(r'^rest-auth/', include('rest_auth.urls')),
#     url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
# ]

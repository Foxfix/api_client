from django.conf.urls import url 
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

from .views import client

urlpatterns = [
    url(r'^token/', obtain_jwt_token),
    url(r'^$', client, name='client'),

    
]


'''
curl -X POST -d "username=olga&password=223355aa" http://127.0.0.1:8090/api/token/
получим токен
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IjFAbWFpbC5ydSIsInVzZXJfaWQiOjE2LCJ1c2VybmFtZSI6Im9sZ2EiLCJleHAiOjE0OTI0NTg3MDZ9.wKM3Lch_3xgnsMg2WpGleCclXctecuiE9GOKiCRxT4Q
отправляем запрос с токеном и получаем доступ к api
curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im9sZ2EiLCJleHAiOjE0OTI0NTk2NjcsImVtYWlsIjoiMUBtYWlsLnJ1IiwidXNlcl9pZCI6MTZ9.BLpXuyxRz7zt1Ni1hSjXpR9CNUxjx4tVAb9wR7VHAuQ" http://127.0.0.1:8090/api/
'''
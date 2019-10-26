from django.urls import path
from chef_user.users import views
from rest_framework import routers
from django.conf.urls import url, include

from chef_user.users.views import (
    user_redirect_view,
)


app_name = "users"

router = routers.SimpleRouter()
router.register(r'user', views.UserViewset)

urlpatterns = [
    path('', include(router.urls)),
    path("~redirect/", view=user_redirect_view, name="redirect"),
]

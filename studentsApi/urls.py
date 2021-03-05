from django.urls import path,include
from rest_framework import routers

from studentsApi import views

router=routers.DefaultRouter()
router.register('Profiles',views.UserProfileView)


urlpatterns = [
   path('',include(router.urls)),
   path('Login/',views.UserLoginView.as_view()),
   path('Logout/',views.UserLogoutView.as_view()),


]
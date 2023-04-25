from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("",views.CreateUserView,basename="user")


urlpatterns = [
    path('token/',views.GenerateTokenView.as_view()),
    path('create/',include(router.urls)),
    path('search/<str:email>/',views.SearchAPIView.as_view()),
]

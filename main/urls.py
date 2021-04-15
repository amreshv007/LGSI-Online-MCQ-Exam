from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
    path('edit-profile', views.editProfile, name="editProfile"),
    path('editfname', views.editfname, name="editfname"),
    path('editlname', views.editlname, name="editlname"),
    path('editpassword', views.editpassword, name="editpassword"),
    path('start/', views.se_pl, name='se_pl'),
    path('result', views.result, name='result'),
    path('pl-result', views.plresult, name='pl-result'),
    path('se-result', views.seresult, name='se-result'),
    path('upload-question',views.uploadq, name='uploadq')
]
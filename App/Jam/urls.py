from django.urls import path
from . import views
from .views import Invest
# from django.contrib.staticfiles.urls import staticfiles_urlpattterns

urlpatterns = [
    path('', views.home, name="home"),
    path('email', views.email, name="email"),
    path('login',views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('invest', Invest.as_view(), name="invest"),
    path('evenodd', views.evenodd, name="evenodd"),
    path('evenorodd', views.evenorodd, name="evenorodd"),

    path('add', views.add, name="add"),
    path('add1', views.add1, name="add1"),
    path('form', views.form, name="form"),
    path('signup_student', views.signup_student, name='signup_student'),
    path('signup_student_output', views.signup_student_output),
    path('showall', views.showall, name='showall'),
    path('delete_record', views.delete_record),
    path('delete', views.delete),
    path('csv', views.csv),
    path('update_record', views.update_record),
    path('update', views.update),
    path('final_update/<int:id>', views.final_update),


    # path('room/<str:pk>/', views.room, name="room"),
    # path('signup/', views.signup, name="signup"),
    # path('login/', views.login, name="login"),
    # path('otp/', views.otp, name="otp"),

]
# urlpatterns+=staticfiles_urlpatterns()
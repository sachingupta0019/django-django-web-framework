from django.urls import path
from StudentRegistration import views
urlpatterns = [
    path('registration/', views.register, name = "register"),
    path('success/',views.thankyou, name = 'thankyou'),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name ="index"),
    path('about/', about, name ="about"),
    path('services/', services, name ="services"),
    path('blog/', blog, name ="blog"),
    path('contact/', contact, name ="contact"),
    path('privacy/', privacy, name ="privacy"),
    path('condition/', terms_condition, name ="condition"),
]

from django.urls import path, include

urlpatterns = [
    path('mealplan/', include('mealplan.urls')),
    path('admins/', include('admins.urls')),
    path('', include('accounts.urls')),
]


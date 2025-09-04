from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(r'tables', views.BookingsViewSet)

urlpatterns = [
    path('menu/items/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

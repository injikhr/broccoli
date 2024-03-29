from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('user', views.UserResponse.as_view()),
    path('user/token', views.UserTokenResponse.as_view()),
    path('user/<str:did>', views.UserDIDResponse.as_view()),
    path('cover-letter', views.CoverLetterResponse.as_view()),
    path('cover-letter/<int:cl_id>', views.CoverLetterIDResponse.as_view()),
    path('position', views.PositionResponse.as_view()),
    path('position/<int:position_id>', views.PositionIDResponse.as_view()),
])

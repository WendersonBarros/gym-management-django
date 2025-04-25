from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("membership/", views.MembershipList.as_view()),
    path("membership/<int:pk>", views.MembershipDetail.as_view()),
    path("member/", views.MemberList.as_view()),
    path("member/<int:pk>", views.MemberDetail.as_view()),
    path("status/", views.MembershipStatusList.as_view()),
    path("status/<int:pk>", views.MembershipStatusDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

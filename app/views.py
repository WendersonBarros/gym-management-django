from .models import Membership, Member, Membership_status
from .serializers import (
    MembershipSerializer,
    MemberSerializer,
    MembershipStatusSerializer,
)
from rest_framework import generics


class MembershipList(generics.ListCreateAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


class MembershipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer

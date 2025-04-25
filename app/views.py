import datetime
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


class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MembershipStatusList(generics.ListCreateAPIView):
    queryset = Membership_status.objects.all()
    serializer_class = MembershipStatusSerializer

    def perform_create(self, serializer):
        membership = serializer.validated_data["current_membership"]

        expiration_date = datetime.date.today() + datetime.timedelta(
            days=membership.duration_in_months * 30
        )
        serializer.save(expiration_date=expiration_date)


class MembershipStatusDetail(generics.RetrieveUpdateAPIView):
    queryset = Membership_status.objects.all()
    serializer_class = MembershipStatusSerializer

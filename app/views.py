import datetime
from django.http import Http404
from .models import Membership, Member, Membership_status
from .serializers import (
    MembershipSerializer,
    MemberSerializer,
    MembershipStatusSerializer,
)
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


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
        serializer.save(
            expiration_date=expiration_date,
            last_membership_renewal=datetime.date.today(),
        )


class MembershipStatusDetail(generics.RetrieveUpdateAPIView):
    queryset = Membership_status.objects.all()
    serializer_class = MembershipStatusSerializer

    def perform_update(self, serializer):
        membership = serializer.validated_data["current_membership"]
        instance = self.get_object()

        base_date = (
            datetime.date.today()
            if datetime.date.today() > instance.expiration_date
            else instance.expiration_date
        )
        expiration_date = base_date + datetime.timedelta(
            days=membership.duration_in_months * 30
        )

        if membership.is_active is False:
            raise ValidationError(
                {"current_membership": "This membership is not active"}
            )

        serializer.save(
            user=instance.user,
            expiration_date=expiration_date,
            last_membership_renewal=datetime.date.today(),
        )


class ValidateMembershipView(GenericAPIView):
    def get_member(self, entry_code):
        try:
            return Member.objects.get(entry_code=entry_code)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        member = self.get_member(self.kwargs.get("entry_code"))
        try:
            membership_status = Membership_status.objects.get(user=member.id)
        except Membership_status.DoesNotExist:
            raise Http404

        today = datetime.date.today()
        expiration_date = membership_status.expiration_date

        if today > expiration_date:
            return Response(
                {"detail": "Membership expired"}, status=status.HTTP_400_BAD_REQUEST
            )

        return Response({"detail": "Membership is active"}, status=status.HTTP_200_OK)

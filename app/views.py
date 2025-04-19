from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Membership, Member, Membership_status
from .serializers import (
    MembershipSerializer,
    MemberSerializer,
    MembershipStatusSerializer,
)


class MembershipList(APIView):
    def get(self, request, format=None):
        memberships = Membership.objects.all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MembershipDetail(APIView):
    def get_object(self, pk):
        try:
            return Membership.objects.get(pk=pk)
        except Membership.DoesNotExist:
            raise Http404

    def get(self, instance, pk, format=None):
        membership = self.get_object(pk)
        serializer = MembershipSerializer(membership)
        return Response(serializer.data)

    def put(self, instance, pk, format=None):
        membership = self.get_object(pk)
        serializer = MembershipSerializer(membership, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        membership = self.get_object(pk)
        membership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

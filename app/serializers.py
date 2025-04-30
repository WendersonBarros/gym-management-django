from rest_framework import serializers
from .models import Member, Membership, Membership_status


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = "__all__"


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class MembershipStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership_status
        fields = "__all__"
        read_only_fields = ["expiration_date", "last_membership_renewal"]

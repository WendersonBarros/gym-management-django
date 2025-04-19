from rest_framework import serializers
from .models import Member, Membership, Membership_status


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ["id", "name", "duration_in_months", "price", "is_active"]

        def create(self, validated_data):
            return Membership.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get("name", instance.name)
            instance.duration_in_months = validated_data.get(
                "duration_in_months", instance.duration_in_months
            )
            instance.price = serializers.get("price", instance.price)
            instance.is_active = serializers.get("is_active", instance.is_active)
            instance.save()
            return instance


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class MembershipStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership_status
        fields = "__all__"

from django.contrib import admin

from .models import Member, Membership, Membership_status

admin.site.register(Member)
admin.site.register(Membership)
admin.site.register(Membership_status)

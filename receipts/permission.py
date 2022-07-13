from rest_framework import permissions


class IsConstractorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or obj.contractor.id == request.user.id:
            return True

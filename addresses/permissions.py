from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions



class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
          request.user.is_authenticated and request.user.is_superuser 
          or request.user.is_authenticated and obj.user.id == request.user.id
        )
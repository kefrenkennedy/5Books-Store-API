from rest_framework import permissions
from rest_framework.views import Request, View


class isUserOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):

        return (
            request.method == "GET"
            or request.user.is_authenticated
            or request.user.is_staff
        )

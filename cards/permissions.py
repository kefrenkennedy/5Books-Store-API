from rest_framework import permissions
from rest_framework.views import Request, View


class IsAdminOrUser(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):

        return request.user.is_authenticated or request.user.is_superuser


class HasObjectPermissionOrIsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        return request.user == obj.user or request.user.is_superuser

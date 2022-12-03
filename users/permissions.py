from rest_framework import permissions
from rest_framework.views import Request, View


class IsAdminOrUser(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        verifyId = bool(str(request.user.id) == str(view.kwargs["pk"]))
        return bool(verifyId or request.user.is_superuser)


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to allow only admins to delete, while others can read.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated

        if request.method == "DELETE":
            return request.user.is_authenticated and request.user.role == "admin"

        return request.user.is_authenticated

class IsAdminForCreate(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user.is_authenticated and request.user.role == 'admin'
        return request.user.is_authenticated

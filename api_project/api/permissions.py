from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Read access is allowed to anyone.
    - Write access (POST, PUT, DELETE) is **only allowed for admins**.
    """

    def has_permission(self, request, view):
        # Safe methods (GET, HEAD, OPTIONS) → Everyone can access
        if request.method in permissions.SAFE_METHODS:
            return True
        # Modify access → Only for admins
        return request.user and request.user.is_staff

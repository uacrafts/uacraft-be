from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class ReadOnlyAdminModifyPermission(BasePermission):
    """
    Custom permission to allow anyone to read objects,
    but only admins to modify them.
    """

    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            if not (request.user and request.user.is_staff):
                raise PermissionDenied(
                    detail='Access denied.',
                    code=status.HTTP_403_FORBIDDEN
                )

        return request.user and request.user.is_staff

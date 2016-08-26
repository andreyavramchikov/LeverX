from rest_framework import permissions

from authentication.models import User


class ManagerPermissions(permissions.BasePermission):
    """
        Reject to make PUT, POST and etc, except GET to users who are not MANAGERS.
    """
    def has_permission(self, request, view):

        if request.method == 'GET':
            return True
        elif not request.user.is_anonymous() and request.user.user_type == User.MANAGER:
            return True
        else:
            return False

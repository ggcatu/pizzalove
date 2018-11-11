from rest_framework.permissions import BasePermission


class SamePk(BasePermission):
    def has_permission(self, request, view):
        user_pk = view.kwargs.get('pk', None)
        if user_pk == request.user.pk:
            return True
        return False

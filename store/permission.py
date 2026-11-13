from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsCustomerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        return obj.customer == request.user


class CanViewStatistics(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('store.can_view_statistics')














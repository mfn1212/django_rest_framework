from rest_framework import permissions


class BlockListPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blocked = Blocklist.objects.filter(ip_addr=ip_addr).exist()
        return not blocked


class IsOunerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsStuffEditorPermission(permissions.DjangoModelPermissions):

    def has_permission(self, request, view):
        """
        if we have any permissin retern true 
        """
        user = request.user
        if user.is_staff:
            if user.has_perm("products_add_product"):
                return True
            if user.has_perm("products_delete_product"):
                return True
            if user.has_perm("products_change_product"):
                return True
            if user.has_perm("products_view_product"):
                return True
        return False
from .permissions import IsStuffEditorPermission
from rest_framework import permissions
from rest_framework import authentication
from .authentication import TokenAuthentication

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStuffEditorPermission]


class AuthenticationMixin():
    authentication_classes = [authentication.SessionAuthentication ,TokenAuthentication]

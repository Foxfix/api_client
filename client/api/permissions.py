from rest_framework import permissions
 
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

# class IsUpdateProfile(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return obj is None or obj.first_name == request.user
              
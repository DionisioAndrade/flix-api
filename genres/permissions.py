""" Permissions for the Genre API """

from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):
    """
    Custom permission class to allow only authenticated users to access the Genre API.
    """
    def has_permission(self, request, view):
        """
        Check if the user is authenticated.
        """
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('genres.view_genre')
        
        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')
        
        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('genres.change_genre')
        
        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')
        
        return False
    
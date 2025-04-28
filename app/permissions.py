""" Global Permissions for the API """

from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):
    """
    Custom permission class to allow only authenticated users to access the API.
    """
    def has_permission(self, request, view):
        """
        Check if the user is authenticated.
        """
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )

        if not model_permission_codename:
            return False

        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(self, method, view):
        """
        Get the model permission codename based on the request method and view.
        """
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_sufix(method)
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None

    def __get_action_sufix(self, method):
        """
        Get the action suffix based on the request method.
        """
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }

        return method_actions.get(method, '')

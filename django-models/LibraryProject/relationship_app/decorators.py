from django.core.exceptions import PermissionDenied

def user_is_admin(user):
    if user.userprofile.role != 'Admin':
        raise PermissionDenied
    return True

def user_is_librarian(user):
    if user.userprofile.role != 'Librarian':
        raise PermissionDenied
    return True

def user_is_member(user):
    if user.userprofile.role != 'Member':
        raise PermissionDenied
    return True

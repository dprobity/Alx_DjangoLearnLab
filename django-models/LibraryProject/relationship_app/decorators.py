# from django.core.exceptions import PermissionDenied

# def user_is_admin(user):
#     if user.userprofile.role != 'Admin':
#         raise PermissionDenied
#     return True

# def user_is_librarian(user):
#     if user.userprofile.role != 'Librarian':
#         raise PermissionDenied
#     return True

# def user_is_member(user):
#     if user.userprofile.role != 'Member':
#         raise PermissionDenied
#     return True


from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test

# ✅ Check if user is an Admin
def user_is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# ✅ Check if user is a Librarian
def user_is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# ✅ Check if user is a Member
def user_is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# ✅ Decorator for Admin-only Access
def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not user_is_admin(request.user):
            raise PermissionDenied  # ❌ Block access if not Admin
        return view_func(request, *args, **kwargs)
    return wrapper

# ✅ Decorator for Librarian-only Access
def librarian_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not user_is_librarian(request.user):
            raise PermissionDenied  # ❌ Block access if not Librarian
        return view_func(request, *args, **kwargs)
    return wrapper

# ✅ Decorator for Member-only Access
def member_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not user_is_member(request.user):
            raise PermissionDenied  # ❌ Block access if not Member
        return view_func(request, *args, **kwargs)
    return wrapper

from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from relationship_app.models import Book

user = User.objects.get(username="your_test_user")  # Replace with your username
content_type = ContentType.objects.get_for_model(Book)

# Add all permissions
permissions = Permission.objects.filter(content_type=content_type)
user.user_permissions.add(*permissions)

# Save and refresh user
user.save()
print(user.get_all_permissions())  # ✅ Check if the permissions are assigned

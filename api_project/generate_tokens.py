import django
import os

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')
django.setup()

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Function to create a token for a user
def generate_token(username):
    try:
        user = User.objects.get(username=username)
        token, created = Token.objects.get_or_create(user=user)
        
        if created:
            print(f"✅ Token created for user '{username}': {token.key}")
        else:
            print(f"🔁 Token already exists for user '{username}': {token.key}")
    except User.DoesNotExist:
        print(f"❌ Error: User '{username}' does not exist. Please create the user first.")

# Ask for a username
if __name__ == "__main__":
    username = input("Enter the username to generate a token for: ")
    generate_token(username)

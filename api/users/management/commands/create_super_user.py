from django.core.management.base import BaseCommand
from api.users.models import CustomUser

class Command(BaseCommand):
    help = "Used to create superuser"

    def handle(self, *args, **options):
        email = input("Enter email: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = CustomUser.objects.create_superuser(
            email=email,
            username=username,
            password=password
        )

        print("SUPER USER CREATED SUCCESSFULLY!")
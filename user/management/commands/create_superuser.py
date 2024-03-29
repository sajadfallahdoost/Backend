from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', '3574')
            self.stdout.write(self.style.SUCCESS(
                'Successfully created a new superuser'))

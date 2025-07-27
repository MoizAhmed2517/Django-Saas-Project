from django.core.management.base import BaseCommand


class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        print("Hello, World! This is a custom Django management command.")
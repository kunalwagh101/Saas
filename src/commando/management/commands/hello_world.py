from django.core.management.base import BaseCommand




class Command(BaseCommand): # Command class must be named Command
    help = 'Prints "Hello, World" to the console'

    def handle(self, *args, **kwargs): # handle method must be named handle
        self.stdout.write('Hello, World')
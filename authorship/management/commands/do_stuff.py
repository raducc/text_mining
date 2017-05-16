from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        import ipdb; ipdb.set_trace()
        print ("ceva")
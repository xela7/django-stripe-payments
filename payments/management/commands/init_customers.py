from django.core.management.base import BaseCommand

from django.contrib.auth import get_user_model

from payments.models import Customer


class Command(BaseCommand):
    
    help = "Create customer objects for existing users that don't have one"
    
    def handle(self, *args, **options):
        user_model = get_user_model()
        for user in user_model.objects.filter(customer__isnull=True):
            Customer.create(user=user)
            print "Created customer for {0}".format(user.email)

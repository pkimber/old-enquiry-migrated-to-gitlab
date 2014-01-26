from django.core.management.base import BaseCommand

from enquiry.tests.scenario import default_scenario_enquiry


class Command(BaseCommand):

    help = "Create demo data for 'enquiry'"

    def handle(self, *args, **options):
        default_scenario_enquiry()
        print("Created 'enquiry' demo data...")

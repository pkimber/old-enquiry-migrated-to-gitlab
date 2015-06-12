# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "Initialise 'enquiry' application"

    def handle(self, *args, **options):
        print("Initialised 'enquiry' app...")

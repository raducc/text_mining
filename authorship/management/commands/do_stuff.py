from django.core.management.base import BaseCommand
from authorship.utils import Features
from pprint import pprint


class Command(BaseCommand):

    def handle(self, *args, **options):
        ee = Features().extract_features('./dataset/charlzdickens/Bleak House.txt')
        pprint(ee)
        ff = Features().extract_features('./dataset/charlzdickens/Hard Times.txt')
        pprint(ff)
        gg = Features().extract_features('./dataset/charlzdickens/Hunted Down.txt')
        pprint(gg)
        print ("")
        ee = Features().extract_features('./dataset/George Eliot/Adam Bede by George Eliot.txt')
        pprint(ee)

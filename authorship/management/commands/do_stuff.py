import json

from django.core.management.base import BaseCommand
from authorship.utils import Features, Trainer
from pprint import pprint
# import settings
from tm import settings


class Command(BaseCommand):

    def handle(self, *args, **options):
        json_file = open(settings.features_file, "r")
        features_json = json_file.read()
        json_file.close()
        features_dict = json.loads(features_json)

        authors_dict = {}
        author_nr = 0
        train_datas = []
        train_authors = []
        for author, features in features_dict.items():
            authors_dict[author_nr] = author
            train_datas.extend(features)
            train_authors.extend([author_nr] * len(features))
            author_nr += 1
        trainer = Trainer()
        trainer.train(train_datas, train_authors)

        ee = Features().extract_features('./dataset/charlzdickens/Bleak House.txt')
        pprint(ee)
        # ff = Features().extract_features('./dataset/charlzdickens/Hard Times.txt')
        # pprint(ff)
        gg = Features().extract_features('./dataset/charlzdickens/Hunted Down.txt')
        # pprint(gg)
        print ("")
        hh = Features().extract_features('./dataset/George Eliot/Adam Bede by George Eliot.txt')
        pprint(hh)
        dd = Trainer()
        dd.train([gg, hh], [0, 1])
        print (dd.predict([ee]))




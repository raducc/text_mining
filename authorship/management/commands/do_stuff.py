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
        test_datas = []
        test_authors = []
        for author, features in features_dict.items():
            authors_dict[author_nr] = author
            train_datas.extend(features[2:])
            train_authors.extend([author_nr] * len(features[2:]))
            test_datas.extend(features[:2])
            test_authors.extend([author_nr] * 2)
            author_nr += 1
        trainer = Trainer()
        trainer.train(train_datas, train_authors)

        author_nr = 0
        for data in test_datas:
            print (trainer.predict([data]), test_authors[author_nr])
            author_nr += 1

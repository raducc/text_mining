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
        test_size = 4
        for author, features in features_dict.items():
            authors_dict[author_nr] = author
            train_datas.extend(features[test_size:])
            train_authors.extend([author_nr] * len(features[test_size:]))
            test_datas.extend(features[:test_size])
            test_authors.extend([author_nr] * test_size)
            author_nr += 1
            # if author_nr > 8:
            #     break
        trainer = Trainer()
        trainer.train(train_datas, train_authors)

        author_nr = 0
        for data in test_datas:
            # if test_authors[author_nr] > 8:
            #     break
            print(test_authors[author_nr], trainer.predict([data]))
            author_nr += 1

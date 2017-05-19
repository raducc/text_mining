import os
import json
from django.core.management.base import BaseCommand
from authorship.utils import Features, Trainer
from pprint import pprint
from tm import settings


class Command(BaseCommand):

    def handle(self, *args, **options):
        authors = os.listdir(settings.dataset_dir)
        features_class = Features()
        features_dict = {}
        features_dict['all_docs_cnt'] = 0
        features_dict['authors'] = {}
        for author in authors:
            print (author)
            features_dict['authors'][author] = {}
            features_dict['authors'][author]['features'], features_dict['authors'][author]['docs_cnt'] = features_class.bayse_extract_features(author)
            features_dict['all_docs_cnt'] += features_dict['authors'][author]['docs_cnt']
        features_json = json.dumps(features_dict)
        json_file = open(settings.bayse_features_file, "w")
        json_file.write(features_json)
        json_file.close()

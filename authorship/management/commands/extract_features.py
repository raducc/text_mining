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
        for author in authors:
            files = os.path.join(settings.dataset_dir, author)
            features_dict[author] = []
            for file in os.listdir(files):
                if os.path.isdir(file):
                    continue
                file_path = os.path.join(settings.dataset_dir, author, file)
                features_dict[author].append(features_class.extract_features(file_path))
                print(file_path)

        features_json = json.dumps(features_dict)
        json_file = open(settings.features_file, "w")
        json_file.write(features_json)
        json_file.close()

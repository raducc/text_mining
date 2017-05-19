import json

import nltk
from django.core.management.base import BaseCommand
from authorship.utils import Features, Trainer
from pprint import pprint
# import settings
from tm import settings


class Command(BaseCommand):

    def handle(self, *args, **options):
        json_file = open(settings.bayse_features_file, "r")
        features_json = json_file.read()
        json_file.close()
        features_dict = json.loads(features_json)

        # _file = open("dataset/anthony trollope/The Way We Live Now.txt", "r")
        _file = open("dataset/charlzdickens/A Childs History of England.txt", "r")
        all_text = _file.read()
        _file.close()
        max_prob = 0
        tokenized_data = nltk.tokenize.word_tokenize(all_text)
        guess = ''
        for author, a_data in features_dict['authors'].items():
            c_prob = a_data['docs_cnt'] / features_dict['all_docs_cnt']
            pos = 0
            for word in Features.features_words:
                c_prob *= pow(a_data['features'][pos], tokenized_data.count(word)/len(tokenized_data))
                pos += 1
            if c_prob > max_prob:
                max_prob = c_prob
                guess = author
        print(guess)

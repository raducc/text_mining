from sklearn.svm import LinearSVC
import math
import nltk
import re


class Features(object):

    def extract_features(self, docname):
        the_docfile = open(docname, "r")
        data = the_docfile.read()
        data = re.sub(r'\s+', ' ', data).replace("\n", " ").lower()
        the_docfile.close()
        tokenized_data = nltk.tokenize.word_tokenize(data)
        total_tokens = len(tokenized_data) / 1000
        features = [
            tokenized_data.count(',') / total_tokens,
            tokenized_data.count(';') / total_tokens,
            (tokenized_data.count('"') + tokenized_data.count("'")) / total_tokens,
            tokenized_data.count('!') / total_tokens,
            tokenized_data.count('-') / total_tokens,
            tokenized_data.count('and') / total_tokens,
            tokenized_data.count('but') / total_tokens,
            tokenized_data.count('however') / total_tokens,
            tokenized_data.count('if') / total_tokens,
            tokenized_data.count('that') / total_tokens,
            tokenized_data.count('more') / total_tokens,
            tokenized_data.count('must') / total_tokens,
            tokenized_data.count('might') / total_tokens,
            tokenized_data.count('this') / total_tokens,
            tokenized_data.count('very') / total_tokens,
        ]

        # mean word length
        regex = re.compile(r'\b((?=\D)[\w]+)\b')
        words = regex.findall(data)
        features.append(len("".join(words)) / len(words))

        # mean sentence length
        sentences = nltk.tokenize.sent_tokenize(data)
        mean_sentence_length = len("".join(sentences)) / len(sentences)
        features.append(mean_sentence_length)

        # Standard Deviation of Sentence Length
        cnt = 0
        for sentence in sentences:
            t = float(len(sentence)) - mean_sentence_length
            cnt += (t*t)
        standard_deviation_sentence = math.sqrt(cnt / len(sentences))
        features.append(standard_deviation_sentence)
        return features


class Trainer(object):

    def __init__(self, training_set=None):
        self.clfr = LinearSVC()

    def train(self, train_datas, train_authors):
        self.clfr.fit(train_datas, train_authors)

    def predict(self, test_data) :
        return self.clfr.predict(test_data)[0]

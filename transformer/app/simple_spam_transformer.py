import nltk
from nltk.corpus import wordnet
import pandas as pd

nltk.download('wordnet')


class SpamFilter:
    def __init__(self):
        self._train_data = pd.read_csv('resources/train_data.csv', encoding='latin-1')

        self._prob_spam = self._train_data['LABEL'].value_counts()['spam'] / self._train_data.shape[0]
        self._prob_ham = self._train_data['LABEL'].value_counts()['ham'] / self._train_data.shape[0]

        self._num_spam = self._train_data.loc[self._train_data['LABEL'] == 'spam', 'SMS'].apply(len).sum()
        self._num_ham = self._train_data.loc[self._train_data['LABEL'] == 'ham', 'SMS'].apply(len).sum()
        self._vocab_size = len(self._train_data.columns) - 3

        self._alpha = 1

    def filter(self, message):
        prob_message_is_spam = self._prob_spam
        prob_message_is_ham = self._prob_ham

        for word in message:
            prob_message_is_spam *= self._prob_if_spam(word)
            prob_message_is_ham *= self._prob_if_ham(word)

        if prob_message_is_spam > prob_message_is_ham:
            return 'spam', prob_message_is_spam, prob_message_is_ham
        else:
            return 'ham', prob_message_is_spam, prob_message_is_ham

    def _prob_if_spam(self, word):
        if word in self._train_data.columns:
            return (self._train_data.loc[self._train_data['LABEL'] == 'spam', word].sum() + self._alpha) / \
                   (self._num_spam + self._alpha * self._vocab_size)
        else:
            return 1

    def _prob_if_ham(self, word):
        if word in self._train_data.columns:
            return (self._train_data.loc[self._train_data['LABEL'] == 'ham', word].sum() + self._alpha) / \
                   (self._num_ham + self._alpha * self._vocab_size)
        else:
            return 1


def similar_messages(message, max_synonyms=None):
    message = message.split()
    synonyms = {}
    indices = {}

    for word_index, word in enumerate(message):
        if word not in synonyms.keys():
            synonyms[word] = wordnet.synsets(word)
            indices[word] = [word_index]
        else:
            indices[word].append(word_index)

    new_messages = []
    original_message = message
    new_message = []

    if max_synonyms is None:
        max_synonyms = max([len(synonym_list) for synonym_list in synonyms.values()])

    for synonym_index in range(0, max_synonyms):
        new_message += original_message
        for word in synonyms.keys():
            word_synonyms = synonyms[word]
            if len(word_synonyms) > 0:
                if len(word_synonyms) > synonym_index:
                    for word_index in indices[word]:
                        new_message[word_index] = word_synonyms[synonym_index].lemmas()[0].name()
                else:
                    for word_index in indices[word]:
                        new_message[word_index] = word_synonyms[-1].lemmas()[0].name()
        new_messages.append(" ".join(new_message))

    return new_messages


class SimpleSpamTransformer:
    def __init__(self):
        self._filter = SpamFilter()

    def transform(self, spam, max_synonyms=None) -> (str, bool):
        similar_spam = similar_messages(spam, max_synonyms)
        if isinstance(spam, float):
            print(spam)

        for similar in similar_spam:
            if self._filter.filter(similar)[0] == 'ham':
                ham = similar
                return ham, True

        return spam, False

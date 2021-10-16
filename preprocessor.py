'''
@author: Sougata Saha
Institute: University at Buffalo
'''

import collections
from nltk.stem import PorterStemmer
import re
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


class Preprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.ps = PorterStemmer()

    def get_doc_id(self, doc):
        """ Splits each line of the document, into doc_id & text.
            Already implemented"""
        arr = doc.split("\t")
        return int(arr[0]), arr[1]

    def tokenizer(self, text):
        lower = text.lower()
        spcl_chrctr = re.sub('[^A-Za-z0-9]+', ' ', lower)
        rem_white = ' '.join(spcl_chrctr.split()).strip()
        terms = rem_white.split(' ')
        rem_stop = [term for term in terms if term not in self.stop_words]
        porter_terms  = [self.ps.stem(term) for term in rem_stop]
        return porter_terms


        """ Implement logic to pre-process & tokenize document text.
            Write the code in such a way that it can be re-used for processing the user's query.
            To be implemented."""
        

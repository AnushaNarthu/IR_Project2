'''
@author: Sougata Saha
Institute: University at Buffalo
'''

from linkedlist import LinkedList
from collections import OrderedDict


class Indexer:
    def __init__(self):
        """ Add more attributes if needed"""
        self.inverted_index = OrderedDict({})

    def get_index(self):
        """ Function to get the index.
            Already implemented."""
        return self.inverted_index

    def generate_inverted_index(self, doc_id, tokenized_document):
        """ This function adds each tokenized document to the index. This in turn uses the function add_to_index
            Already implemented."""
        for t in tokenized_document:
            self.add_to_index(t, doc_id)

    def add_to_index(self, term_, doc_id_):
        if term_ in self.inverted_index.keys():
            posting_list = self.inverted_index[term_]
            list1 = posting_list.traverse_list()
            if doc_id_ not in list1:
                posting_list.insert_at_end(doc_id_)
                self.inverted_index[term_] = posting_list
            else:
                m = posting_list.start_node
                while m is not None:
                    if m.value == doc_id_:
                        m.count_terms+=1
                        break
                    m = m.next
        else:
            posting_list = LinkedList()
            posting_list.insert_at_end(doc_id_)
            self.inverted_index[term_] = posting_list

        """ This function adds each term & document id to the index.
            If a term is not present in the index, then add the term to the index & initialize a new postings list (linked list).
            If a term is present, then add the document to the appropriate position in the posstings list of the term.
            To be implemented."""

        

    def sort_terms(self):
        """ Sorting the index by terms.
            Already implemented."""
        sorted_index = OrderedDict({})
        for k in sorted(self.inverted_index.keys()):
            sorted_index[k] = self.inverted_index[k]
        self.inverted_index = sorted_index

    def add_skip_connections(self):
        for value in self.inverted_index.keys():
            pointer = self.inverted_index[value]
            pointer.add_skip_connections()

        """ For each postings list in the index, add skip pointers.
            To be implemented."""
            
        return

    def calculate_tf_idf(self,docs_count,docs):
        for value in self.inverted_index.values():
            m = value.start_node
            while m is not None:
                count_term = len(docs[m.value])
                doc_freq = value.length
                term_freq = m.count_terms/count_term
                docs_count = docs_count
                idf = docs_count/doc_freq
                m.tf_idf = term_freq*idf
                #print(m.tf_idf)
                m = m.next
                """ Calculate tf-idf score for each document in the postings lists of the index.
              To be implemented."""
        return
        
        
    

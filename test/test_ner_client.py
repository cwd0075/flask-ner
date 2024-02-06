import unittest
from ner_client import NamedEntityClient

class TestNerClient(unittest.TestCase):

    def test_get_ents_returns_dictionary_given_empty_string_causes_empty_spacy_doc_ents(self):
        ner = NamedEntityClient()
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)



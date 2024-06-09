import unittest
from auto_suggest import auto_suggest

class TestAutoSuggest(unittest.TestCase):
    def test_empty_input(self):
        words = []
        prefix = "ke"
        suggestions = auto_suggest(words, prefix)
        self.assertEqual(suggestions, [])

    def test_no_suggestions(self):
        words = ["take", "make", "check", "ack", "rake"]
        prefix = "xyz"
        suggestions = auto_suggest(words, prefix)
        self.assertEqual(suggestions, [])

    def test_single_suggestion(self):
        words = ["take", "make", "check", "ack", "rake"]
        prefix = "rak"
        suggestions = auto_suggest(words, prefix)
        self.assertEqual(suggestions, ["rake"])

    def test_multiple_suggestions(self):
        words = ["take", "make", "check", "ack", "rake"]
        prefix = "ke"
        suggestions = auto_suggest(words, prefix)
        self.assertEqual(sorted(suggestions), ["check", "make", "rake", "take"])

    def test_wildcard_prefix(self):
        words = ["take", "make", "check", "ack", "rake"]
        prefix = "*k"
        suggestions = auto_suggest(words, prefix)
        self.assertEqual(sorted(suggestions), ["ack", "check"])

if __name__ == '__main__':
    unittest.main()
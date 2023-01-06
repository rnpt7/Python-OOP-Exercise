"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Finds a random word from a text file

    >>> finder = WordFinder("test_words.txt")
    3 words read

    >>> finder.random() in ["cat", "dog", "porcupine"]
    True

    >>> finder.random() in ["cat", "dog", "porcupine"]
    True
    """
    def __init__(self, path):
        """Read the file and return number of words"""
        with open(path, "r") as f:
            text = f.read()
            self.words = text.split()
        print(f"{len(self.words)} words read")

    def random(self):
        """Returns a random word from the list of words read from path"""
        return random.choice(self.words)

class AdvWordFinder(WordFinder):
    """Advanced WordFinder that ignores comments and empty lines

    >>> adv_finder = AdvWordFinder("adv_test_words")
    4 words read

    >>> adv_finder.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> adv_finder.random() in ["kale", "parsnips", "apple", "mango"]
    True
    """
    def __init__(self, path):
        """Read the file, ignoring empty lines and comments, and makes a word list"""
        with open(path, "r") as f:
            lines = f.readlines()
            self.words = []
            for line in lines:
                # Ignores lines starting with "#" or that are empty
                if not line.startswith("#") and line.strip():
                    self.words.extend(line.split())
        print(f"{len(self.words)} words read")

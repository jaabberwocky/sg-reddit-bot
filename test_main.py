from unittest.mock import MagicMock
import unittest
from main import is_alphabetical_order, has_69_char


class TestRedditBot(unittest.TestCase):
    def setUp(self):
        self.comment = MagicMock()
        self.comment.body = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.comment.subreddit = MagicMock()
        self.comment.subreddit.display_name = "asksingapore"
        self.reddit = MagicMock()

    def test_is_alphabetical_order(self):
        self.assertTrue(is_alphabetical_order("abcdefghijklmnopqrstuvwxyz"))
        self.assertFalse(is_alphabetical_order("afbec"))

    def test_has_69_char(self):
        self.assertFalse(has_69_char(
            "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        self.assertFalse(has_69_char(
            "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGH"))

    def test_bot(self):
        self.reddit.subreddit.return_value.stream.comments.return_value = [
            self.comment]

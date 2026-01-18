import unittest
from logic import get_github_url

class TestLogic(unittest.TestCase):
    def test_url_creation(self):
        result = get_github_url("octocat")
        self.assertEqual(result, "https://api.github.com/users/octocat")
    def test_empty_user(self):
        result = get_github_url("")
        self.assertIsNone(result)
if(__name__ == '__main__'):
    unittest.main()

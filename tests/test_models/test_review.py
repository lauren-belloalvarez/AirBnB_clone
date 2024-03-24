#!/user/bin/python3
"""
Module Review's Test Case
"""
import unittest
from models.review import Review


class TestingReview(unittest.TestCase):

    def test_review_attributes(self):
        # Testing review attributes
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()

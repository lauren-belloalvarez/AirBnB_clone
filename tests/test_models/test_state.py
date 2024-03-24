#!usr/bin/python3
"""
State Module's Test Case
"""
import unittest
from models.state import State


class TestingState(unittest.TestCase):

    def test_attributes_state(self):
        # Testing state attributes
        state = State()
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()

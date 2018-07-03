import unittest
from lootbag import *

# check for issues
class check_for_issues(unittest.TestCase):

    # check if you can add child name
    def test_if_you_can_set_name_and_toys(self):
        test = loot.add_toys('Larry', ['meth', 'motorcycle', 'burning hot liquids'])
        self.assertEqual(test[name], 'Larry')

    # check if you can add toys
    def test_if_you_can_add_toys(self):
        test = loot.add_toys('Larry', ['meth', 'motorcycle', 'burning hot liquids'])
        self.assertIn('meth', test[toys])

    # Items can be removed from bag, per child.
    def test_if_you_can_remove_toys(self):
        test = loot.add_toys('Larry', ['meth', 'motorcycle', 'burning hot liquids'])
        toys = loot.remove_toys('Larry', ['meth'])
        self.assertNotIn('meth', toys)

    # Removing ball from the bag should not be allowed. A child's name must be specified.

    # Must be able to list all children who are getting a toy.

    # Must be able to list all toys for a given child's name.

    # Must be able to set the delivered property of a child, which defaults to false to true.

if __name__  == '__main__':
    unittest.main()
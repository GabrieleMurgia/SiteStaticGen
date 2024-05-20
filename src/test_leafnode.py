import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    
    def test_props_to_html(self):
       node1 = LeafNode("p", "This is a paragraph of text.")
       node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

       node1_to_html = node1.to_html()
       expected_1 = '<p>This is a paragraph of text.</p>'
       node2_to_html = node2.to_html()
       expected_2 = '<a href="https://www.google.com">Click me!</a>'

       self.assertEqual(node1_to_html,expected_1)
       self.assertEqual(node2_to_html,expected_2)

if __name__ == "__main__":
    unittest.main()
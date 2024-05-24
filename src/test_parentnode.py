import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    
    def test_props_to_html(self):
       node1 = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )
       
    

       node1_to_html = node1.to_html()
       expected_1 = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
       expected_html =  "<PARENT><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></PARENT>"

       self.assertEqual(node1_to_html,expected_1)
       self.assertEqual(node1_to_html,expected_html)

if __name__ == "__main__":
    unittest.main()
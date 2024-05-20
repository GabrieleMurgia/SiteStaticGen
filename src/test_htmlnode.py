import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
       child_node = HTMLNode("a", "Clicca qui", None, {"href": "https://www.example.com"})
       node = HTMLNode('p', 'test paragraph', [child_node], {"href": "https://www.google.com"})
       node2 = HTMLNode('p', 'test paragraph', [child_node], {"href": "https://www.google.com"})
       self.assertEqual(node, node2)
    
    def test_props_to_html(self):
       node1 = HTMLNode('p', 'test paragraph',"", {"href": "https://www.google.com", "target": "_blank"})
       string_node = 'href="https://www.google.com" target="_blank"'

       self.assertEqual(node1.props_to_html(),string_node)

if __name__ == "__main__":
    unittest.main()
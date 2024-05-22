from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)


    def to_html(self):
        if self.tag is None:
            raise ValueError("You should provide a tag")
        elif self.children is None:
            raise ValueError("You should provide a children")
        else:
            temp_string = ""
            for i in range(0, len(self.children)):
                current_child = self.children[i]
                temp_string += current_child.to_html()
            return f"<{self.tag}>{temp_string}</{self.tag}>"
                


node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

node2 = ParentNode(
    "PARENT",
    [
        ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
),
                ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
),
                ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
),
                ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
),
    ],
)

#rint(node.to_html())
print(node2.to_html())
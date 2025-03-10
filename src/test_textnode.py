import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a test node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a test node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a test node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

    def test_none(self):
        node = TextNode("This is a test node", TextType.BOLD_TEXT, None)
        response = "This is a test node, bold"
    
if __name__ == "__main__":
    unittest.main()
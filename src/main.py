from textnode import TextNode
from textnode import TextType
# print("hello world")

def main():
    new_node = TextNode("Anchor text", TextType.LINK_TEXT, None)
    print(new_node)


main()
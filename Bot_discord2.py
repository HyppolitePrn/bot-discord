from Bot_discord3 import Node

root = Node("A","B")


root.insert_node(Node("B","C"), "A")
root.insert_node(Node("H","V"), "A")
root.insert_node(Node("F","D"), "B")
root.insert_node(Node("tg","pd"), "B")
root.insert_node(Node("hello","salut"), "F")
current_node = root
keyword = input()


def get_current_node(current_node,keyword):

    print(current_node.question)
    for Node in current_node.list_child_node:
        if keyword == Node.keyword:
            current_node = Node.question
            return current_node
        else:
            if len(Node.list_child_node) > 0:
                for Node in Node.list_child_node:
                        # print(Node.question)
                        get_current_node(Node, keyword)


print(get_current_node(current_node,keyword))
# if keyword == keyword:
#     current_node = question
#     current_node
# elif len(list_child_node) > 0:
#     for child_node in .list_child_node:
#         if child_node.keyword == keyword:
#             current_node = child_node.question
#             return current_node


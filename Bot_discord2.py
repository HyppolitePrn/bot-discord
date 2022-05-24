from Bot_discord3 import Node

root = Node("A","B")

root.insert_node(Node("B","C"), "A")
root.insert_node(Node("F","D"), "B")
print('salut')
print(root.list_child_node[0].list_child_node[0].question)



class Node :
    def __init__(self,question,keyword):
        self.question = question
        self.keyword = keyword
        self.list_child_node = []
    
    def insert_node(self, Node, question):
        if self.question == question:
            self.list_child_node.append(Node)
        elif len(self.list_child_node) > 0:
            for child_node in self.list_child_node:
                child_node.insert_node(Node, question)


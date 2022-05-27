from calendar import c
from threading import currentThread
from Bot_discord3 import Node

root = Node("Comment puis-je vous aider ?", "help")


root.insert_node(Node("Dans quelle language souhaitez-vous obtenir des informations ?",
                 "tuto"), "Comment puis-je vous aider ?")

root.insert_node(Node("Je vous conseille de regarder cette playlist pour toutes informations sur le HTML : https://youtube.com/playlist?list=PL4cUxeGkcC9ivBf_eKCPIAYXWzLlPAm6G",
                 "html"), "Dans quelle language souhaitez-vous obtenir des informations ?")
root.insert_node(Node("Je vous conseille de regarder cette playlist pour toutes informations sur le CSS : https://youtube.com/playlist?list=PL4cUxeGkcC9ivBf_eKCPIAYXWzLlPAm6G",
                 "css"), "Dans quelle language souhaitez-vous obtenir des informations ?")
root.insert_node(Node("Je vous conseille de regarder cette playlist pour toutes informations sur le PHP : https://youtube.com/playlist?list=PLjwdMgw5TTLVDv-ceONHM_C19dPW1MAMD",
                 "php"), "Dans quelle language souhaitez-vous obtenir des informations ?")
root.insert_node(Node("Je vous conseille de regarder cette playlist pour toutes informations sur le python : https://youtube.com/playlist?list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR",
                 "python"), "Dans quelle language souhaitez-vous obtenir des informations ?")
root.insert_node(Node("Je vous conseille de regarder cette playlist pour toutes informations sur le Javascript : https://youtube.com/playlist?list=PL4cUxeGkcC9haFPT7J25Q9GRB_ZkFrQAc",
                 "javascript"), "Dans quelle language souhaitez-vous obtenir des informations ?")

root.insert_node(Node("De quel language voulez-vous la documentation ?",
                 "documentation"), "Comment puis-je vous aider ?")

root.insert_node(Node("Voici la documentation de JavaScript : https://developer.mozilla.org/fr/docs/Web/JavaScript",
                 "javascript"), "De quel language voulez-vous la documentation ?")
root.insert_node(Node("Voici la documentation de HTML : https://developer.mozilla.org/fr/docs/Web/HTML",
                 "html"), "De quel language voulez-vous la documentation ?")
root.insert_node(Node("Voici la documentation de CSS : https://developer.mozilla.org/fr/docs/Web/CSS",
                 "css"), "De quel language voulez-vous la documentation ?")
root.insert_node(Node("Voici la documentation de Python : https://www.python.org/",
                 "python"), "De quel language voulez-vous la documentation ?")
root.insert_node(Node("Voici la documentation de PHP : https://www.php.net/manual/fr/intro-whatis.php",
                 "php"), "De quel language voulez-vous la documentation ?")


def get_current_node(current_node, keyword):
    print(current_node.question)

    for Node in current_node.list_child_node:
        if keyword == Node.keyword:
            current_node = Node.question
            return current_node

        else:
            if len(Node.list_child_node) > 0:
                return get_current_node(Node, keyword)


def get_current_node_2(current_node, keyword):
    for Node in current_node.list_child_node:

        if keyword == Node.keyword:
            current_node = Node.question
            return current_node
        else:
            for Node in Node.list_child_node:
                if len(Node.list_child_node) > 0:
                    print(Node.question, 'dans le else')
                    match = get_current_node_2(Node, keyword)
                    print(match, 'match')
                    if match:
                        return match


def get_enfant_direct(current_node, keyword):
    print(len(current_node.list_child_node))
    if len(current_node.list_child_node) > 0:
        for Node in current_node.list_child_node:
            if keyword == Node.keyword:
                current_node = Node
                return current_node

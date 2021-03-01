from Words import words

class TrieNode(object):
    def __init__(self,char:str):
        self.char=char
        self.children=[]
        self.word_finished=False
        

def add(root,word:str):
    node =root
    for char in word:
        found_in_child=False
        for child in node.children:
            if child.char==char:
                
                node=child
                found_in_child=True
                break
        if not found_in_child:
            new_node=TrieNode(char)
            node.children.append(new_node)
            node=new_node
    node.word_finished=True

def find_word(root,word:str):
    node=root
    for char in word:
        found_in_child=False
        for child in node.children:
            if child.char==char:
                node =child
                found_in_child=True
                break
        if not found_in_child:
            return False
    if(node.word_finished==True):
        return True
    return False


def initiate():
    root = TrieNode('*')
    add(root, "hackathon")
    add(root, 'hack')
    for word in words:
        add(root,word)
    return root
    


    
    


            

    
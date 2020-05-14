'''
Stylometric Search Engine
'''

# Imports

import os
from nltk.parse import stanford
os.environ['STANFORD_PARSER'] = './StanfordNLP/stanford-parser-full-2018-10-17'
os.environ['STANFORD_MODELS'] = './StanfordNLP/stanford-parser-full-2018-10-17'

class Tree:

    def __init__(self,value):
        self.value = value
        self.tree = None
        self.generate_tree()

    def generate_tree(self):
        sp = stanford.StanfordParser()
        tree = list(sp.raw_parse(self.value))[0]
        self.tree = tree
        return
    
    def clean_tree(self):
        for node in self.tree.treepositions('leaves'):
            del(self.tree[node])

    def subtree(self,height):
        sub_trees = []
        for st in self.tree.subtrees(lambda t: t.height() == height):
            sub_trees.append(st)
        return sub_trees
'''
t = Tree("My dog also likes eating sausage on the weekend.")
t.clean_tree()
t.tree.pretty_print()
subtrees = t.subtree(2)

for i in subtrees:
    i.pretty_print()

'''





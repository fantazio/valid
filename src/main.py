#! /usr/bin/env python

operators = { '!': (lambda x : not (x[0].eval()))
            , '=>' : (lambda x : x[0].eval() or not x[1].eval())
            , '<=>' : (lambda x : x[0].eval() == x[1].eval())
            , '&' : (lambda x : x[0].eval() and x[1].eval())
            , '|' : (lambda x : x[0].eval() or x[1].eval())}

# a node is composed of a value and sons (if it is a parent node)

truths = []

class Node:

    def __init__(self, value, sons):
        self.value = value
        self.sons = sons

    def eval(self):
        self.reduce()
        if type(self.value) == type(True): # Boolean value as expected
            return self.value
        else:
            print 'Error: cannot evaluate expression'
            return False

    def reduce(self):
        for son in self.sons:
            son.reduce()
        if type(self.value) == type(''): # Value not computed yet
            if self.sons == []:
                self.value = self.value in truths
            else:
                self.value = operators[self.value](self.sons)

    def __str__(self):
        if len(self.sons) > 1:
            return (self.sons[0].__str__() + ' ' + self.value + ' ' + self.sons[1].__str__())
        elif len(self.sons) > 0:
            return (self.value + ' ' + self.sons[0].__str__())
        else:
            return self.value



def parse(sons = [], op = [False]):
    if op[0] not in operators.keys():
        node = Node(op[0], sons)
        if len(op) > 1:
            return parse(sons = [node], op = op[1:])
        else:
            return node
    else:
        return Node(op[0], sons + [parse(sons = [], op = op[1:])])



def main():
    truths = raw_input().strip().split(' ')

    for truth in truths:
        if truth in operators.keys():
            return 'Error: operator detected in truths'

    res = parse(op = raw_input().strip().split(' ')).eval()
    return res

print main()

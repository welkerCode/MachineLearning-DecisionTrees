
class Node:

    def __init__(self):
        self.children = {}
        self.splittingAttr = None

    def getChildren(self):
        return self.children

    def printNode(self):
        s1 = "I am a node. My children are: \n"
        childStrings = []
        for child in self.children:
            childStrings.append("\t" + child.printNode())
        children = ""
        for child in childStrings:
            children = children + child
        return s1 + children

    def prediction(self, attributes):
        desiredAttribute = self.splittingAttr
        potentialChildren = self.children
        return potentialChildren[attributes[desiredAttribute]].prediction(attributes)
class Leaf:

    def __init__(self, label):
        self.label = label

    def getLabel(self):
        return self.label

    def printNode(self):
        return "I am a Leaf.  My label is: " + str(self.label) + "\n"

    def prediction(self,attributes):
        return self.label